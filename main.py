from tldextract import extract
from sshtunnel import SSHTunnelForwarder
from datetime import datetime, timedelta
import pymysql
import json
import os
import subprocess
import calendar
from collections import defaultdict
import re


dev_bastion_host = "3.38.97.146"
dev_bastion_user = "ubuntu"
dev_bastion_key = "/Users/taehoon/.conn/rework_seoul.pem"
# 퍼플릭 ip
bastion_host = "3.34.91.110"
bastion_user = "ubuntu"
bastion_key = "/Users/taehoon/.conn/rework_seoul_prod_bastion.pem"

# ec2_host = "172.33.4.254"
# ec2_user = "ubuntu"

# redis 주소
dev_db_host = "172.31.78.125"
dev_db_user = "root"
dev_db_pass = "qwerasdf"
dev_db_name = "clogo_dev"
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
rds_read_host = "officemail-io.cluster-ro-cbtlgq57tl3u.ap-northeast-2.rds.amazonaws.com"
rds_write_host = "officemail-io.cluster-cbtlgq57tl3u.ap-northeast-2.rds.amazonaws.com"
rds_user = "root"
rds_password = "3731WfJ7s7S0EB0w6fW80"

domain_list = []
log_domain_list = []
final_log_domain_list = []
uniq_list = []


d = []
now = datetime.today()
file_date = now.strftime("%Y-%m-%d")
# file_date = "2024-05-20"
m = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
year = datetime.now().year
last_month = datetime.now().month - 1
format_month = "{:02}".format(last_month)


def load_db_data():
    with SSHTunnelForwarder(
        (bastion_host, 22),
        ssh_username=bastion_user,
        ssh_pkey=bastion_key,
        remote_bind_address=(
            rds_read_host,
            3306,
        ),
    ) as tunnel:
        conn = pymysql.connect(
            host="localhost",
            port=tunnel.local_bind_port,
            user=rds_user,
            passwd=rds_password,
            db="company_logo",
        )

        # tunnel.start()

        # global domain_list
        # domain_list = []
        try:
            with conn.cursor() as cur:
                # cur.execute("show databases")

                cur.execute("select domain from company_logo;")
                for r in cur:
                    # print(r[0])
                    domain_list.append(r[0])
            # print(domain_list)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cur.close()
            print("load_data OK")
        # print(json.dumps(domain_list, indent=2, ensure_ascii=False), len(domain_list))

    #########################################

    # 1. os.system("ls -la > xxx.log")
    # with open("xxx.log", "r") as fr:
    # buf = fr.read()

    # str_cmd = "ls -la > xxx.log"
    # 2. subprocess.open(str_cmd.split())


def log_contrast_with_db():
    with open(
        f"/Users/taehoon/logs/daily_top_request_domain_{file_date}.log", "r"
    ) as f:
        lines = f.readlines()
        for line in lines:
            first_domain = line.split()[1].replace("\n", "")
            parse_domain = extract(first_domain, include_psl_private_domains=False)

            # is_subdomain = parse_domain.subdomain

            domain_without_subdomain = parse_domain.registered_domain
            domain_without_subdomain_count = int(line.split()[0])

            if domain_without_subdomain == "":
                break

            log_domain_list.append(
                [int(domain_without_subdomain_count), domain_without_subdomain]
            )

        final_log_domain_list.append([0, 0])

        # 로그 안에 있는 동일 도메인 하나로 합침
        for log_domain_item in log_domain_list:
            count = 0
            for final_domain_item in final_log_domain_list:
                if log_domain_item[1] in final_domain_item:
                    count += 1
                    final_domain_item[0] += log_domain_item[0]
            if count == 0:
                final_log_domain_list.append([log_domain_item[0], log_domain_item[1]])
        # DB 에 있는 도메인
        for final_list_item in final_log_domain_list:
            count = 0
            for domain_list_item in domain_list:
                if final_list_item[1] == domain_list_item:
                    count += 1
                    break
            if count == 0:
                uniq_list.append(final_list_item)

        # uniq_list.pop(0)
        uniq_list.sort(reverse=True)

        with open(f"/Users/taehoon/logs/no_filter_result_{file_date}.log", "a") as ff:
            for i in uniq_list:
                ff.write(f"{i}\n")
    print("log_contrast_with_db OK")
    delete_file(f"/Users/taehoon/logs/daily_top_request_domain_{file_date}.log")


def input_deactivate_data():
    # 운영
    with SSHTunnelForwarder(
        (bastion_host, 22),
        ssh_username=bastion_user,
        ssh_pkey=bastion_key,
        remote_bind_address=(
            rds_write_host,
            3306,
        ),
    ) as tunnel:
        conn = pymysql.connect(
            host="localhost",
            port=tunnel.local_bind_port,
            user=rds_user,
            passwd=rds_password,
            db="company_logo",
        )
        # 계발
        # with SSHTunnelForwarder(
        #     (dev_bastion_host, 22),
        #     ssh_username=dev_bastion_user,
        #     ssh_pkey=dev_bastion_key,
        #     remote_bind_address=(
        #         dev_db_host,
        #         3306,
        #     ),
        # ) as tunnel:
        #     conn = pymysql.connect(
        #         host="localhost",
        #         port=tunnel.local_bind_port,
        #         user=dev_db_user,
        #         passwd=dev_db_pass,
        #         db=dev_db_name,
        #     )

        with conn.cursor() as cur:
            from datetime import datetime

            count = 0
            with open(
                f"/Users/taehoon/logs/{datetime.now().month}-{datetime.now().day}_log_sum_sort.log",
                "r",
            ) as f:
                a = f.readlines()
                for i in range(len(a)):
                    if count == 10:
                        break
                    domain = (
                        a[i].split(",")[1].replace("]\n", "").replace("'", "").lstrip()
                    )
                    # hit_rate = int(i.split(",")[0].replace("[", ""))
                    # query_domain_result = (
                    #     cur.query(CompanyLogoDailyDB)
                    #     .filter(CompanyLogoDailyDB.domain == domain)
                    #     .first()
                    # )

                    cur.execute("select domain, hash from company_logo;")
                    # cur.fetchall()
                    exist_db = 0
                    for db_domain in cur:
                        if domain in db_domain:
                            exist_db += 1
                            break
                        # if domain in db_domain and len(hash) <= 30:
                        #     # print(db_domain)
                        #     # print(str(db_domain))
                        #     # print(str(db_domain).split(",")[2])
                        #     print(str(db_domain).split(",")[2])
                        #     db_hit_rate = int(
                        #         str(db_domain)
                        #         .split(",")[2]
                        #         .replace(" ", "")
                        #         .replace(")", "")
                        #     )
                        #     db_hit_rate += hit_rate
                        #     # print(db_domain)
                        #     add_value = domain + "zzz"
                        #     cur.execute(
                        #         f"update company_logo set test={db_hit_rate} where domain=%s;",
                        #         (domain),
                        #     )
                        #     conn.commit()
                    d = datetime.utcnow() + timedelta(hours=9)
                    if exist_db == 0:
                        cur.execute(
                            f"insert into company_logo (domain, title, hash, created_at, updated_at) VALUES (%s, %s, %s, %s, %s);",
                            (domain, "", "", d, d),
                        )

                        conn.commit()
                        count += 1
            cur.close()


def without_one_five_log():
    with open(f"/Users/taehoon/logs/no_filter_result_{file_date}.log") as f:
        a = f.readlines()
        for i in a:
            if int(i.split(",")[0].replace("[", "")) >= 5:
                domain = i.split(",")[1].replace("]\n", "").replace("'", "").lstrip()
                hit_rate = int(i.split(",")[0].replace("[", ""))
                with open(f"/Users/taehoon/logs/result_{file_date}.log", "a") as ff:
                    ff.write(f"[{hit_rate}, {domain}]\n")
    print("without_one_five_log OK")
    delete_file(f"/Users/taehoon/logs/no_filter_result_{file_date}.log")


def delete_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)
        print("remove ok")
    else:
        print("no search file_path")


def sum_log():
    make_file_path = (
        f"/Users/taehoon/logs/{datetime.now().month}-{datetime.now().day}_log_sum.log"
    )
    today = datetime.today()
    # for day in range(calendar.monthrange(year, last_month)[1]):
    for day in range(29, -1, -1):
        date = today - timedelta(days=day)

        format_day = "{:02}".format(date.day)
        format_month = "{:02}".format(date.month)

        # read_file_path = f"/Users/taehoon/logs/final_result_{year}-{format_month}-{format_day}.log"
        read_file_path = (
            f"/Users/taehoon/logs/result_{year}-{format_month}-{format_day}.log"
        )

        if os.path.isfile(read_file_path) == True:
            with open(read_file_path, "r") as f:
                r = f.read()
                with open(make_file_path, "a") as ff:
                    ff.write(r)
        else:
            continue
    print("sum_log OK")


def sum_log_sort():
    domain_pattern = re.compile(r"^[a-zA-Z0-9.-]{2,}\.[a-zA-Z]{2,}$")

    with open(
        f"/Users/taehoon/logs/{datetime.now().month}-{datetime.now().day}_log_sum.log"
    ) as f:
        temprory_domain_list = []
        a = f.readlines()
        for i in a:
            domain = i.split()[1].replace("\n", "").replace("]", "")
            count = i.split()[0].replace("[", "").replace(",", "")

            if domain_pattern.match(domain):
                temprory_domain_list.append([count, domain])
            else:
                pass

        domain_counts = defaultdict(int)
        for count, domain in temprory_domain_list:
            domain_counts[domain] += int(count)

        # 원하는 출력 형식으로 다시 변환
        result = [[count, domain] for domain, count in domain_counts.items()]
        result.sort(reverse=True)

        with open(
            f"/Users/taehoon/logs/{datetime.now().month}-{datetime.now().day}_log_sum_sort.log",
            "a",
        ) as ff:
            for i in result:
                ff.write(f"{i}\n")


# 가공된 기본 로그 생성 -> daily_top_request_domain.log 파일 생성
command = "sh /Users/taehoon/make_log_file.sh"
os.system(command)


# DB에서 데이터 불러옴
load_db_data()


# 규격화된 로그 DB 파일로 생성 -> no_filter_result.log 파일 생성 및 daily_top_request_domain.log 파일 삭제
log_contrast_with_db()
#
#
# # # 5이상의 도메인만 로그 파일로 다시 생성;; -> result.log 파일 생성 및 no_filter_result.log 파일 삭제
without_one_five_log()
#
# if (
#     datetime.now().day
#     == calendar.monthrange(datetime.now().year, datetime.now().month)[1]
# ):
# 한달치 로그 합침 -> monthly_log_sum.log 파일 생성
# sum_log()
# #     #
# #     # # 한달치 로그 합친것을 소트
# sum_log_sort()
#
# DB 데이터와 비교하여 일정 수준의 Request 를 받은 도메인 DB 에 등록
# input_deactivate_data()

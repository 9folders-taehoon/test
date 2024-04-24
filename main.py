from tldextract import extract
from sshtunnel import SSHTunnelForwarder
from datetime import datetime, timedelta
import pymysql
import json
import os
import subprocess


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
            with open(f"/Users/taehoon/logs/result_{file_date}.log") as f:
                a = f.readlines()
                for i in a:
                    if int(i.split(",")[0].replace("[", "")) >= 20:
                        domain = (
                            i.split(",")[1].replace("]\n", "").replace("'", "").lstrip()
                        )
                        hit_rate = int(i.split(",")[0].replace("[", ""))
                        # query_domain_result = (
                        #     cur.query(CompanyLogoDailyDB)
                        #     .filter(CompanyLogoDailyDB.domain == domain)
                        #     .first()
                        # )

                        cur.execute("select domain, hash from company_logo;")
                        cur.fetchall()
                        counter = 0
                        for db_domain in cur:
                            # hash = str(db_domain).split(",")[1]
                            if domain in db_domain:
                                counter += 1
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
                        import datetime

                        d = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
                        if counter == 0:
                            cur.execute(
                                f"insert into company_logo (domain, title, hash, created_at, updated_at) VALUES (%s, %s, %s, %s, %s);",
                                (domain, "", "", d, d),
                            )

                        conn.commit()
            cur.close()

        # logo = CompanyLogoDailyDB()
        # if query_domain_result:
        #     query_domain_result.hit_rate += hit_rate
        # else:
        #     logo.domain = domain
        #     logo.hit_rate = hit_rate
        #     d.append(logo)

        # print(i.split(",")[1].replace("]\n", "").replace("'", "").lstrip())
        # print(int(i.split(",")[0].replace("[", "")))
    # session.add_all(d)
    # session.commit()


# local
# with db_session() as session:
#     with open(f"/Users/taehoon/logs/result_{file_date}.log") as f:
#         a = f.readlines()
#         for i in a:
#             if int(i.split(",")[0].replace("[", "")) >= 10:
#                 domain = (
#                     i.split(",")[1].replace("]\n", "").replace("'", "").lstrip()
#                 )
#                 hit_rate = int(i.split(",")[0].replace("[", ""))
#                 query_domain_result = (
#                     session.query(CompanyLogoDailyDB)
#                     .filter(CompanyLogoDailyDB.domain == domain)
#                     .first()
#                 )
#                 logo = CompanyLogoDailyDB()
#                 if query_domain_result:
#                     query_domain_result.hit_rate += hit_rate
#                 else:
#                     logo.domain = domain
#                     logo.hit_rate = hit_rate
#                     d.append(logo)
#
#                 # print(i.split(",")[1].replace("]\n", "").replace("'", "").lstrip())
#                 # print(int(i.split(",")[0].replace("[", "")))
#     session.add_all(d)
#     session.commit()


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
        a = f.readlines()
        for i in a:
            first_domain = i.split()[1].replace("\n", "")
            parse_domain = extract(first_domain, include_psl_private_domains=False)

            is_subdomain = parse_domain.subdomain

            domain_without_subdomain = parse_domain.registered_domain
            domain_without_subdomain_count = int(i.split()[0])
            if domain_without_subdomain == "":
                continue
            log_domain_list.append(
                [int(domain_without_subdomain_count), domain_without_subdomain]
            )
        final_log_domain_list.append([0, 0])
        for test in log_domain_list:
            count = 0
            for test2 in final_log_domain_list:
                if test[1] in test2:
                    count += 1
                    test2[0] += test[0]
            if count == 0:
                final_log_domain_list.append([test[0], test[1]])
        del final_log_domain_list[-1]
        # print(json.dumps(final_log_domain_list))

        for i in final_log_domain_list:
            count = 0
            # print(i)
            for j in domain_list:
                if i[1] == j:
                    count += 1
                    break
            if count == 0:
                uniq_list.append(i)

        # uniq_list.pop(0)
        uniq_list.sort(reverse=True)

        # print(type(domain_list), domain_list)
        # for i in log_domain_list:
        #     if "google.com" in domain_list:
        #         uniq_list.append("google.com")
        #         print(uniq_list)

        # a = i.split()[1].replace("\n", "")
        with open(f"/Users/taehoon/logs/result_{file_date}.log", "a") as ff:
            for i in uniq_list:
                ff.write(f"{i}\n")


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 운영 서버 db에 넣기
def input_data():
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

        # tunnel.start()

        # global domain_list
        # domain_list = []
        try:
            with conn.cursor() as cur:
                # cur.execute("show databases")
                cur.execute(
                    "insert into company_logo (domain, title, hash) VALUES ('mango.com', 'mango', '111');"
                )
                conn.commit()
            # print(domain_list)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cur.close()

        # print(json.dumps(domain_list, indent=2, ensure_ascii=False), len(domain_list))


def without_one_two_log():
    with open(f"/Users/taehoon/logs/result_{file_date}.log") as f:
        a = f.readlines()
        for i in a:
            if int(i.split(",")[0].replace("[", "")) >= 5:
                domain = i.split(",")[1].replace("]\n", "").replace("'", "").lstrip()
                hit_rate = int(i.split(",")[0].replace("[", ""))
                with open("beaty", "a") as ff:
                    ff.write(f"[{hit_rate}, {domain}]\n")


# 가공된 기본 로그 생성
# command = "sh /Users/taehoon/make_log_file.sh"
# os.system(command)


# DB에서 데이터 불러옴
# load_db_data()


# 규격화된 로그 파일로 생성
# log_contrast_with_db()


# 5이상의 도메인만 로그 파일로 다시 생성;;
without_one_two_log()


# DB 데이터와 비교하여 일정 수준의 Request 를 받은 도메인 DB 에 등록
# input_deactivate_data()

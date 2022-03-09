# !/bin/python3
import jenkins
import json


def create_jenkins_iob(data):
    # 登录jenkins
    server = jenkins.Jenkins(
        'http://uh.haier.net/jenkins/',
        username='baseline',
        password='11b84952f9f8c9e87e6ee5f044acdb7c8a')
    server.build_job(
        "testFlightUpload",
        parameters={
            "baseline": json.dumps(data)})

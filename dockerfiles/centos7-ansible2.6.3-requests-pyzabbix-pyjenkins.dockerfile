FROM centos7
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN yum install -y ansible-2.6.3
RUN yum install -y python-pip
RUN pip install python-jenkins & pip install requests & pip install requests-html & pip install pyzabbix

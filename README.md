ec2-pricing-rest-api
====================

Rest API server with EC2 pricing for ondemand and reserved instances 

REST server built on top of https://github.com/erans/ec2instancespricing by
Eran Sandler

#API design

HTTP Method | URI | Action
:---------: | --- | ------
GET | /api/[type] | Retrieve list of `ondemand` or `reserved` type of instances
GET | /api/[type]/[region] | Retrieve list of instances filtered for a specific region: ``` us-east-1 us-west-1 us-west-2 eu-west-1 ap-southeast-1 ap-southeast-2 ap-northeast-1 sa-east-1 ```
GET | /api/[type]/[size] | Retrieve list of instances filtered by size: ``` t1.micro m1.small m1.medium m1.large m1.xlarge m2.xlarge m2.2xlarge m2.4xlarge m3.medium m3.large m3.xlarge m3.2xlarge c1.medium c1.xlarge c3.xlarge c3.2xlarge c3.4xlarge c3.8xlarge cc2.8xlarge cg1.4xlarge cr1.8xlarge hi1.4xlarge hs1.8xlarge g2.2xlarge r3.large r3.xlarge r3.2xlarge r3.4xlarge r3.8xlarge i2.xlarge i2.4xlarge i2.8xlarge ```
GET | /api/[type]/[os] | Retrieve list of instances filtered by OS type: ``` linux mswin rhel sles mswinSQL mswinSQLWeb ```

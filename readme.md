Project Name : S3-PAYMENT-AUTOAUDIT

Description : A application where a file is uploaded and its type and details are extracted and stored in the DB.Auto Audit happens i.e certain business rules are validated automatically
and the ones which require manual audit are displayed explicitly.

Installation :
        1) Django - https://docs.djangoproject.com/en/2.2/topics/install/
        2) Pandas Package - pip3 install pandas
        3) DateTime Package - pip3 install datetime
        4) Rules Package - pip3 install rules

Usage :
        1)Clone the above repository.
        2)Run command "python3 manage.py runserver".
        3)Open the url obtained.Home Page Appears.
        
        FILE UPLOAD
        1)In the Home Page,Click on File Upload Option.
        2)Choose a File and the Type correctly and Submit.
        3)Details are updated and redirected to Home Page.Check the Updated Details here.  

        AUTO AUDIT
        1)In the Home Page,Click on Manual Audit Option.
        2)Once the link is clicked, Auto Audit occurs.Once done all those records that failed    to validate automatically (require manual audit) are displayed.
        3)Check according to the business rules, that only records that failed validation are    displayed.

### Docker build

``` docker-compose build ```

### Docker run

``` docker-compose up```


*** Settings ***
Library     DataDriver  file=../Resources/Datas/City.csv
Resource  ../Configurations/ConfigurationMaps.robot
Test Template  Checking Same From To Template
Suite Teardown  Close Browser

*** Keywords ***
Checking Same From To Template
    [Arguments]  ${City}
    New Browser  chromium    headless=False
    New Page    ${Endpoint}
    Fill Text    ${From}    ${City}
    Click    ${FromList1}
    Fill Text    ${To}    ${City}
    Click    ${ToList1}
    Wait For Alert    action=accept    text=Ayni Sehri Secemezsiniz   timeout=${TIMEOUT}

*** Test Cases ***
Checking Same City in From and To : ${City}
    [Tags]    DDD

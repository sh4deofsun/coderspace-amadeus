*** Settings ***

Resource  ../Configurations/ConfigurationMaps.robot
Library     DataDriver   file=../Resources/Datas/CityXCity.csv  dialect=excel
# Library     DataDriver   file=../Resources/Datas/CC.csv  dialect=excel
Test Template     Checking flights numbers template
Suite Teardown  Close Browser

*** Test Cases ***
Checking flights numbers between ${City1} and ${City2}
    
*** Keywords ***

Checking flights numbers template
    [Arguments]  ${City1}  ${City2}
    New Browser  chromium    headless=False
    New Page    ${Endpoint}
    Log    ${City1}
    Log    ${City2}
    Clear Text    ${From}
    Fill Text    ${From}    ${City1}
    Click    ${FromList1}
    Clear Text    ${To}
    Fill Text    ${To}    ${City2}
    Click    ${ToList1}
    ${Status}  Run Keyword And Return Status    Compare
    Run Keyword If    ${Status}
    ...    Pass Execution  PASS
    ...  ELSE
    ...    Fail

Compare
    ${Count}  Get Element Count    role=list >> li                     
    Log    ${Count}
    ${T}  Get Text    .mb-10
    @{W}  Split String    ${T}
    ${C}  Convert To Integer    ${W}[1]
    Should Be Equal    ${Count}    ${C}
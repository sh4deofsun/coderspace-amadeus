*** Settings ***
Resource  ../Configurations/ConfigurationMaps.robot

*** Test Cases ***

Calling Test API
    ${Response}  Call Api    Test
    Set Suite Variable    ${Response}

Checking Test API Content-Type
    Depends On Test    Calling Test API
    Should Be Equal As Strings    ${Response}[ResponseHeader][Content-Type]    application/json

Checking Test API Data Type
    Depends On Test    Calling Test API
    FOR    ${element}    IN    @{Response}[ResponseData][data]
        Log    ${element}
        Variable Type Should Be  int  ${element}[id]
        Variable Type Should Be  str  ${element}[from]
        Variable Type Should Be  str  ${element}[to]
        Variable Type Should Be  str  ${element}[date]
    END
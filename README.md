[comment]: # "Auto-generated SOAR connector documentation"
# SSL Labs

Publisher: Splunk  
Connector Version: 2\.0\.2  
Product Vendor: Qualys  
Product Name: SSL Labs  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.9\.39220  

This app supports executing investigative actions to analyze a host

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a SSL Labs asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**base\_url** |  optional  | string | Base URL
**verify\_server\_cert** |  required  | boolean | Verify server certificate

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity\. This action runs a quick query on the device to check the connection and credentials  
[run query](#action-run-query) - Run SSL Labs analysis of a host  

## action: 'test connectivity'
Validate the asset configuration for connectivity\. This action runs a quick query on the device to check the connection and credentials

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'run query'
Run SSL Labs analysis of a host

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**host** |  required  | Host address ie\. www\.qualys\.com | string |  `domain` 
**publish** |  optional  | Publish report publicly \(\[off\]/on\) | string | 
**start\_new** |  optional  | Start a new assessment \(\[off\]/on\) | string | 
**max\_age** |  optional  | Maximum age in hours of the cached report\. If the value passed is less than or equal to 0 it will consider default to 12 | numeric | 
**return\_all\_data** |  optional  | Return full information \(\[off\]/on\) | string | 
**ignore\_mismatch** |  optional  | Proceed with assessments even when the server certificate doesn't match the assessment hostname\. Set to off by default\. Please note that this parameter is ignored if a cached report is returned | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.host | string |  `domain` 
action\_result\.parameter\.ignore\_mismatch | string | 
action\_result\.parameter\.max\_age | numeric | 
action\_result\.parameter\.publish | string | 
action\_result\.parameter\.return\_all\_data | string | 
action\_result\.parameter\.start\_new | string | 
action\_result\.data\.\*\.criteriaVersion | string | 
action\_result\.data\.\*\.endpoints\.\*\.delegation | numeric | 
action\_result\.data\.\*\.endpoints\.\*\.duration | numeric | 
action\_result\.data\.\*\.endpoints\.\*\.eta | numeric | 
action\_result\.data\.\*\.endpoints\.\*\.grade | string | 
action\_result\.data\.\*\.endpoints\.\*\.gradeTrustIgnored | string | 
action\_result\.data\.\*\.endpoints\.\*\.hasWarnings | boolean | 
action\_result\.data\.\*\.endpoints\.\*\.ipAddress | string |  `ip` 
action\_result\.data\.\*\.endpoints\.\*\.isExceptional | boolean | 
action\_result\.data\.\*\.endpoints\.\*\.progress | numeric | 
action\_result\.data\.\*\.endpoints\.\*\.serverName | string |  `domain` 
action\_result\.data\.\*\.endpoints\.\*\.statusMessage | string | 
action\_result\.data\.\*\.engineVersion | string | 
action\_result\.data\.\*\.host | string | 
action\_result\.data\.\*\.isPublic | boolean | 
action\_result\.data\.\*\.port | numeric | 
action\_result\.data\.\*\.protocol | string | 
action\_result\.data\.\*\.startTime | numeric | 
action\_result\.data\.\*\.status | string | 
action\_result\.data\.\*\.testTime | numeric | 
action\_result\.summary\.total\_endpoints | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
## Introduction to Dynamic Vlan Trunking 
Cisco gives many more on vlan trunking configuration for dynamically negotiating trunking configuration, Basically, Switch will negotiate that it will start trunking, not start trunking and identify whether to start trunk or not this called as Dynamic Trunking Protocol (DTP). Cisco switches use the switchport mode interface command to define dynamic trunking Protocol. 


## Misson 
- To complete this lab, You should need to troubleshoot all the errors that network faces and try to make network work. 


# Hints

- Always check vlan Administrative mode because it defines the property of dynamic trunking protocol
- The following table will help you to troubleshoot this lab

<table>
<tr>
<td> 

## Dynamic Trunking Protocol Options

|    Command Options   | Description                                                                                                 |                                                                                                                                                                          
|----------------------|-------------------------------------------------------------------------------------------------------------|
| access               |  not trunking                                                                                               |                                                                                                    
|                      |                                                                                                             |                                                                                                                                                                                                               
| trunk                |   Always trunking                                                                                          |                                                                                                                                                                                        
| dynamic desirable    |    Send negotiation messages and response to negotiation messages, to dynamically chose to start trunking    |                                                                                         
| dynamic auto         |   always waits to receive trunk negotiation message from connected switch, Whenever, recevied trunking negotiation message then start trunking.                                                                                                                             |                                                                                                                                                                                                                                  
</td>
</tr>
</table>

Thank You




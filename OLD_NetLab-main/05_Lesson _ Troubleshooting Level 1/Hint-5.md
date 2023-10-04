## Interface are not Working Status
Cisco switches use two different sets of status code. One set of the two status codes that are also used in router's interface status code and another set of one status code(Word).

Let's talk about Single status Code which is basically a word that tells either the interface is working or not, i.e (Connected, notconnect). Now, what about the two status codes refering the line status and protocol status.
The Line status tells about layer 1's working and Protocol status tells about the layer 2's working. 

## Misson 
 - In this lab, You will have to troubleshoot the interface and find the problem .


## Hint 
- The following table list is given for the code combination and defining some problems that are commonly occuring on interfaces.

<table>
<tr>
<td> 

## Switch inteface Status Code

|    Line Status       | Protocol Status      | Interface Status | Description                                                                                                                                                                            | 
|----------------------|----------------------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Administratively Down|  Down                | Disabled         |      Interface was not working because of the command was used on it                                                                                                                   | 
|                      |                      |                  |                                                                                                                                                                                        | 
| Down                 |   Down               | notconnect       |     Might be possible, that there is no cable, wrong cable pinouts, or there is sometime speed mismatch, or there is possiblity the neigboring deice is powered off, or error-disabled |       
|                      |                      |                  |                                                                                                                                                                                        | 
| Up                   |    Down              | notconnect       |    Not expected on lan switch physical interfaces                                                                                                                                      |   
|                      |                      |                  |                                                                                                                                                                                        |      
| Down                 |   Down(Err-Disabled) | err-disabled     |    Port security has been disabled the interface                                                                                                                                       |       
|                      |                      |                  |                                                                                                                                                                                        |
| up                   |   up                 |  Connected       |       The interface is working perfectly                                                                                                                                               |     

</td>
</tr>
</table>


Thank You

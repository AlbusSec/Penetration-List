## Introduction to Etherchannel load distribution 

Etherchannel also handles load that was generated from interfaces. But it doesn't distribute the traffic equally among the links. Means the traffic doesn't go on a distributed state. The etherchannel uses hash algorithms to forward packets from etherchannels. The calculated load balancing hash determines which physical interface will be used by etherchannel to forward frame.


## Misson

- Verify that the network engineer correctly configured the EtherChannel, If yes then leave and if not then configure whole thing in the network.
- Analyze the load balancing method. Therefore, If the switch uses the src mac method for load balancing, then change it into sec-dst-mac.


## Hint

- Use some show command to verify the etherchannl configurations.

Thank You

## 【predict】

Name : (Variables)_(What to predict)  

pdp : probe_dst_prefix  
rsa : reply_src_addr  
ttl : probe_ttl  

pdp_ttl : predict probe_ttl based on probe_dst_prefix   
rsa_ttl : predict probe_dst_prefix based on reply_src_addr   
pdp_rsa : predict reply_src_addr based on probe_dst_prefix    
rsa_pdp : predict probe_dst_prefix based on reply_src_addr  

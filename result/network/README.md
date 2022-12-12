# 【network (internet topology map)】 

File name: Time_(the number of "Probe_dst_prefix")_(the number of "Reply_src_addr")  


For visualizing Internet topology of Iris dataset, I used pyvis (library for quick generation of visual network graphs with python code), and NetworkX (Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks).  


## Workflow of graphing Internet topology  


1. Draw a node of “Probe_src_addr” (this value is fixed, 132.227.123.8)  
2. Draw nodes of “Reply_src_addr”  
3. Draw edges between “Probe_src_addr” and “Reply_src_addr” with Blue line  
4. Draw nodes of “Probe_dst_prefix”  
5. Draw edges between “Reply_src_addr” and “Probe_dst_prefix” with Red line  


Size of node: “Probe_dst_prefix” (invisible) << “Reply_src_addr” (visible small) << “Probe_src_addr” (large)  
Blue line: Probe_src_addr — Reply_src_addr  
Red line: Reply_src_addr — Probe_dst_prefix  

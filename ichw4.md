# 作业4
1. **作业、进程、线程的概念:**

    作业是指用户向计算机提交的任务实体。(通常体现为用户运行一个程序)
  
    进程是指计算机为了完成用户任务实体而设置的执行实体，是向系统申请分配资源的基本单位。
  
    线程是进程中某个单一顺序的控制流，也就是一个进程下的多个能独立运行的更小的单位。在引入线程的操作系统中，通常都是把进程作为分配资源的基本单位，而把线程作为独立运行和独立调度的基本单位。
  
    **进程和线程概念的提出分别解决的问题：**
  
    现代计算机的 CPU 和多数 I/O 设备同一时刻只能处理一个任务，进程实现了资源的分配和调度，满足了多道程序的各个程序同时运行的需求。
  
    由于线程比进程更小，基本上不拥有系统资源，故对它的调度所付出的开销就会小得多，能更高效的提高系统多个程序间并发执行的程度。
  
2. **调研虚拟存储器的概念:**

    虚拟存储器是由操作系统提供的一个假想的特大存储器。电脑中所执行的程序占用内存很大或很多时，则会导致内存消耗殆尽。为解决该问题，Windows通过匀出一部分硬盘空间来充当内存使用。当内存耗尽时，电脑就会自动调用硬盘来充当内存，以缓解内存的紧张。
    
    **虚拟存储器的工作原理和作用：**
    
    工作原理：每个进程都有一个抽象的地址空间，进程1访问物理内存中的数据时，它获得的地址是抽象的虚拟地址，硬件MMU可将虚拟地址翻译为物理地址，然而物理内存是有限的，虚拟存储技术将每个进程常用的加载到内存中，不用的先暂存到磁盘，需要它时再从磁盘中将它加载出来。如果物理内存中有数据就传送给cpu，如果没有就产生异常，然后内存和磁盘进程数据交换后再由内存将数据传送给cpu。
    
    作用：虚拟存储器解决了进程并发问题(当使用同样虚拟内存地址的两个软件同时在电脑运行时。翻译器会将同样的虚拟内存地址映射到不同的实际内存地址，从而使软件之间不发生冲突；但使用同样物理内存地址的两个软件是无法同时在电脑上运行的)及内存空间不够用的问题(已在上述内容中解释)。

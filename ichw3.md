# 作业3
**通用的高速缓存存储器结构及工作原理：**

　　Cache的组成部分分为标记存储器和数据存储器，前者储存Cache的控制位(管理Cache的读写操作)和块地址标签(记录Cache中各块的地址)。块地址标签记录的地址包含了与主内存映射的块地址，且都与Cache中的一块“数据”相对应。Cache能将CPU用过的数据及结果保存起来，使得CPU下次处理时先来访问Cache，如果没有可用的数据再去别处找，以此来提高运行速度。

　　当CPU读取数据时，先通过地址总线把物理地址送到Cache中，与Cache中的块地址标签进行对比。若相符合，则表示此数据已经存在于Cache中（称为“命中”），这时只需把Cache中的对应数据经由数据总线直接传送给CPU即可。但如果CPU送来的物理地址无法与Cache中的块地址标签相符，则表明这一数据不在Cache中（称为“失误”），这时，需要从主内存把CPU所需的数据地址拷贝到Cache中，再由Cache把数据传送给CPU。显然，如果CPU读取命中的话，存取速度比直接访问主内存要快得多，但倘若失误，则速度反而更慢了，因而常采用适当的映射方式和块替代方式来提高命中率，实现快速的读取速度。

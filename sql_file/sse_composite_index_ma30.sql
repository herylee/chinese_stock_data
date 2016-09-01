-- 上证指数(000001)30日均线
-- SSE(Shanghai Stock Exchange) Composite Index MA 30

create table sse_composite_index_ma30 (
    exchange_date date primary key, -- 日期
    begin_date date, -- 开始日期
    avg_index varchar(10), -- 收盘价平均值
    last_avg_index varchar(10) -- 上一个工作日的收盘价平均值
);
    

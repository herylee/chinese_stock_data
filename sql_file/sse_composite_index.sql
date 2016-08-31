-- 上证指数(000001)
-- SSE(Shanghai Stock Exchange) Composite Index
-- 在不可预计的未来，数字的变化是未知的，因此使用varchar保存数值信息

create table sse_composite_index (
    exchange_date date primary key, -- 日期
    end_index varchar(10), -- 收盘价
    max_index varchar(10), -- 最高价
    min_index varchar(10), -- 最低价
    begin_index varchar(10), -- 开盘价
    last_index varchar(10), -- 前收盘
    rise_fall_index varchar(10), -- 涨跌额
    rise_fall_perc varchar(10), -- 涨跌幅(单位%)
    volume varchar(10), -- 成交量
    amount varchar(13) -- 成交金额
);
    

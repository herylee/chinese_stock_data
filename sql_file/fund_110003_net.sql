-- 易方达上证50指数(110003)基金净值

create table fund_110003_net(
    exchange_date date primary key, -- 日期
    unit_net varchar(7), -- 单位净值
    accumulated_net varchar(7), -- 累计净值
    rise_fall_perc varchar(7) -- 涨跌幅(%)    
);

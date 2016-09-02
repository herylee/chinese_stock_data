-- 易方达上证50指数(110003)基金分红

create table fund_110003_bouns(
    equity_register_date date primary key, -- 权益登记日 
    exclude_dividend_date date, -- 除息日 
    bouns varchar(6), -- 每份分红    
    dividend_payment_date date -- 分红发放日 
);

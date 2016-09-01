-- 上证指数的当天指数/30日均线/60日均线/90日均线

create view sse_composite_index_ma_compare as
select s.exchange_date as exchange_date, s.end_index as end_index, s3.avg_index as avg_index_ma30, s6.avg_index as avg_index_ma60, s9.avg_index as avg_index_ma90
from sse_composite_index as s inner join sse_composite_index_ma30 as s3 on s.exchange_date = s3.exchange_date
                              inner join sse_composite_index_ma60 as s6 on s.exchange_date = s6.exchange_date
                              inner join sse_composite_index_ma90 as s9 on s.exchange_date = s9.exchange_date;

/* Using this dataset, show the SQL query to find the rolling 3 day average transaction amount for each day in January 2021. */

-- get data down to a day level
with t as (
select transaction_time::date as transaction_date,
  sum(transaction_amount) as trx_amt_agg,
  count(1) as trx
from transactions
group by 1
order by 1 desc
)
-- sum amt / trx# to get average (avoids avg of avg)
select transaction_date,
sum(trx_amt_agg)
over (order by transaction_date
      rows between 2 preceding and current row) /
sum(trx)
over (order by transaction_date
      rows between 2 preceding and current row) as r3da
from t
order by 1 desc

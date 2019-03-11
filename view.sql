-- Create view of most popular articles.
CREATE OR REPLACE VIEW themes as
    SELECT distinct(count(log.path)) as eyepoint, log.path
    FROM log
    WHERE log.status = '200 OK'
    and log.path like '/article/%'
    GROUP BY log.path
    ORDER BY eyepoint desc;

-- Create a view of total calls per day.
CREATE OR REPLACE VIEW themetot as
    SELECT COUNT(*) as tot, date_trunc('day', log.time) as date
    FROM log
    GROUP BY date;

-- Create a view of failed calls per day.
CREATE OR REPLACE VIEW themefail as
    SELECT COUNT(*) as fail, date_trunc('day', log.time) as date
    FROM log
	WHERE status != '200 OK'
    GROUP BY date;

-- Create a view of the percentage of failed calls per day.
CREATE OR REPLACE VIEW strengthcall as
    SELECT round((lgntf.fail*1.0/lgntt.tot)*100, 1)
    as misscall, lgntf.date
	FROM themefail as lgntf, themetot as lgntt
    WHERE lgntf.date=lgntt.date;

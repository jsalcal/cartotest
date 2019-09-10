-- TABLE paystats
DROP TABLE public.paystats CASCADE;
CREATE TABLE public.paystats
(    
    amount DOUBLE PRECISION,
    p_month DATE,
    p_age character varying,
    p_gender character varying,
    postal_code_id character varying,
    id INTEGER,
    CONSTRAINT paystats_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)

-- TABLE postal_codes
DROP TABLE public.postal_codes CASCADE;
CREATE TABLE public.postal_codes
(    
    the_geom geometry(MultiPolygon, 4326),
    code character varying,
    id INTEGER,
    CONSTRAINT postal_codes_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)


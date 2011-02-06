--
-- PostgreSQL database dump
--

-- Started on 2011-02-05 21:11:24 EST

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

--
-- TOC entry 1842 (class 1262 OID 16384)
-- Name: robobird; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE robobird WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.utf8' LC_CTYPE = 'en_US.utf8';


ALTER DATABASE robobird OWNER TO postgres;

\connect robobird

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

--
-- TOC entry 352 (class 2612 OID 16485)
-- Name: plpgsql; Type: PROCEDURAL LANGUAGE; Schema: -; Owner: postgres
--

CREATE PROCEDURAL LANGUAGE plpgsql;


ALTER PROCEDURAL LANGUAGE plpgsql OWNER TO postgres;

SET search_path = public, pg_catalog;

--
-- TOC entry 348 (class 1247 OID 16467)
-- Dependencies: 3 1542
-- Name: dblink_pkey_results; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE dblink_pkey_results AS (
	"position" integer,
	colname text
);


ALTER TYPE public.dblink_pkey_results OWNER TO postgres;

--
-- TOC entry 58 (class 1255 OID 16521)
-- Dependencies: 3 352
-- Name: checkinword(text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION checkinword(wxyz text) RETURNS void
    LANGUAGE plpgsql
    AS $_$
DECLARE lcw text;
BEGIN
lcw := lower($1);
--INSERT INTO "Words" ("Word", "Status", "Lang", "InsertDate") VALUES(wxyz, 0, '', now());
INSERT INTO "Words" ("Word") VALUES(lcw);
EXCEPTION WHEN unique_violation THEN
--do tonthing
END;
$_$;


ALTER FUNCTION public.checkinword(wxyz text) OWNER TO postgres;

--
-- TOC entry 39 (class 1255 OID 16457)
-- Dependencies: 3
-- Name: dblink(text, text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink(text, text) RETURNS SETOF record
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_record';


ALTER FUNCTION public.dblink(text, text) OWNER TO postgres;

--
-- TOC entry 40 (class 1255 OID 16458)
-- Dependencies: 3
-- Name: dblink(text, text, boolean); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink(text, text, boolean) RETURNS SETOF record
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_record';


ALTER FUNCTION public.dblink(text, text, boolean) OWNER TO postgres;

--
-- TOC entry 41 (class 1255 OID 16459)
-- Dependencies: 3
-- Name: dblink(text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink(text) RETURNS SETOF record
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_record';


ALTER FUNCTION public.dblink(text) OWNER TO postgres;

--
-- TOC entry 42 (class 1255 OID 16460)
-- Dependencies: 3
-- Name: dblink(text, boolean); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink(text, boolean) RETURNS SETOF record
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_record';


ALTER FUNCTION public.dblink(text, boolean) OWNER TO postgres;

--
-- TOC entry 49 (class 1255 OID 16470)
-- Dependencies: 3
-- Name: dblink_build_sql_delete(text, int2vector, integer, text[]); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_build_sql_delete(text, int2vector, integer, text[]) RETURNS text
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_build_sql_delete';


ALTER FUNCTION public.dblink_build_sql_delete(text, int2vector, integer, text[]) OWNER TO postgres;

--
-- TOC entry 48 (class 1255 OID 16469)
-- Dependencies: 3
-- Name: dblink_build_sql_insert(text, int2vector, integer, text[], text[]); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_build_sql_insert(text, int2vector, integer, text[], text[]) RETURNS text
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_build_sql_insert';


ALTER FUNCTION public.dblink_build_sql_insert(text, int2vector, integer, text[], text[]) OWNER TO postgres;

--
-- TOC entry 19 (class 1255 OID 16471)
-- Dependencies: 3
-- Name: dblink_build_sql_update(text, int2vector, integer, text[], text[]); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_build_sql_update(text, int2vector, integer, text[], text[]) RETURNS text
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_build_sql_update';


ALTER FUNCTION public.dblink_build_sql_update(text, int2vector, integer, text[], text[]) OWNER TO postgres;

--
-- TOC entry 55 (class 1255 OID 16478)
-- Dependencies: 3
-- Name: dblink_cancel_query(text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_cancel_query(text) RETURNS text
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_cancel_query';


ALTER FUNCTION public.dblink_cancel_query(text) OWNER TO postgres;

--
-- TOC entry 35 (class 1255 OID 16453)
-- Dependencies: 3
-- Name: dblink_close(text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_close(text) RETURNS text
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_close';


ALTER FUNCTION public.dblink_close(text) OWNER TO postgres;

--
-- TOC entry 36 (class 1255 OID 16454)
-- Dependencies: 3
-- Name: dblink_close(text, boolean); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_close(text, boolean) RETURNS text
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_close';


ALTER FUNCTION public.dblink_close(text, boolean) OWNER TO postgres;

--
-- TOC entry 37 (class 1255 OID 16455)
-- Dependencies: 3
-- Name: dblink_close(text, text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_close(text, text) RETURNS text
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_close';


ALTER FUNCTION public.dblink_close(text, text) OWNER TO postgres;

--
-- TOC entry 38 (class 1255 OID 16456)
-- Dependencies: 3
-- Name: dblink_close(text, text, boolean); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_close(text, text, boolean) RETURNS text
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_close';


ALTER FUNCTION public.dblink_close(text, text, boolean) OWNER TO postgres;

--
-- TOC entry 20 (class 1255 OID 16439)
-- Dependencies: 3
-- Name: dblink_connect(text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_connect(text) RETURNS text
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_connect';


ALTER FUNCTION public.dblink_connect(text) OWNER TO postgres;

--
-- TOC entry 21 (class 1255 OID 16440)
-- Dependencies: 3
-- Name: dblink_connect(text, text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_connect(text, text) RETURNS text
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_connect';


ALTER FUNCTION public.dblink_connect(text, text) OWNER TO postgres;

--
-- TOC entry 23 (class 1255 OID 16441)
-- Dependencies: 3
-- Name: dblink_connect_u(text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_connect_u(text) RETURNS text
    LANGUAGE c STRICT SECURITY DEFINER
    AS '$libdir/dblink', 'dblink_connect';


ALTER FUNCTION public.dblink_connect_u(text) OWNER TO postgres;

--
-- TOC entry 24 (class 1255 OID 16442)
-- Dependencies: 3
-- Name: dblink_connect_u(text, text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_connect_u(text, text) RETURNS text
    LANGUAGE c STRICT SECURITY DEFINER
    AS '$libdir/dblink', 'dblink_connect';


ALTER FUNCTION public.dblink_connect_u(text, text) OWNER TO postgres;

--
-- TOC entry 22 (class 1255 OID 16472)
-- Dependencies: 3
-- Name: dblink_current_query(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_current_query() RETURNS text
    LANGUAGE c
    AS '$libdir/dblink', 'dblink_current_query';


ALTER FUNCTION public.dblink_current_query() OWNER TO postgres;

--
-- TOC entry 25 (class 1255 OID 16443)
-- Dependencies: 3
-- Name: dblink_disconnect(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_disconnect() RETURNS text
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_disconnect';


ALTER FUNCTION public.dblink_disconnect() OWNER TO postgres;

--
-- TOC entry 26 (class 1255 OID 16444)
-- Dependencies: 3
-- Name: dblink_disconnect(text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_disconnect(text) RETURNS text
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_disconnect';


ALTER FUNCTION public.dblink_disconnect(text) OWNER TO postgres;

--
-- TOC entry 56 (class 1255 OID 16479)
-- Dependencies: 3
-- Name: dblink_error_message(text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_error_message(text) RETURNS text
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_error_message';


ALTER FUNCTION public.dblink_error_message(text) OWNER TO postgres;

--
-- TOC entry 43 (class 1255 OID 16461)
-- Dependencies: 3
-- Name: dblink_exec(text, text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_exec(text, text) RETURNS text
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_exec';


ALTER FUNCTION public.dblink_exec(text, text) OWNER TO postgres;

--
-- TOC entry 44 (class 1255 OID 16462)
-- Dependencies: 3
-- Name: dblink_exec(text, text, boolean); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_exec(text, text, boolean) RETURNS text
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_exec';


ALTER FUNCTION public.dblink_exec(text, text, boolean) OWNER TO postgres;

--
-- TOC entry 45 (class 1255 OID 16463)
-- Dependencies: 3
-- Name: dblink_exec(text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_exec(text) RETURNS text
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_exec';


ALTER FUNCTION public.dblink_exec(text) OWNER TO postgres;

--
-- TOC entry 46 (class 1255 OID 16464)
-- Dependencies: 3
-- Name: dblink_exec(text, boolean); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_exec(text, boolean) RETURNS text
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_exec';


ALTER FUNCTION public.dblink_exec(text, boolean) OWNER TO postgres;

--
-- TOC entry 31 (class 1255 OID 16449)
-- Dependencies: 3
-- Name: dblink_fetch(text, integer); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_fetch(text, integer) RETURNS SETOF record
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_fetch';


ALTER FUNCTION public.dblink_fetch(text, integer) OWNER TO postgres;

--
-- TOC entry 32 (class 1255 OID 16450)
-- Dependencies: 3
-- Name: dblink_fetch(text, integer, boolean); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_fetch(text, integer, boolean) RETURNS SETOF record
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_fetch';


ALTER FUNCTION public.dblink_fetch(text, integer, boolean) OWNER TO postgres;

--
-- TOC entry 33 (class 1255 OID 16451)
-- Dependencies: 3
-- Name: dblink_fetch(text, text, integer); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_fetch(text, text, integer) RETURNS SETOF record
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_fetch';


ALTER FUNCTION public.dblink_fetch(text, text, integer) OWNER TO postgres;

--
-- TOC entry 34 (class 1255 OID 16452)
-- Dependencies: 3
-- Name: dblink_fetch(text, text, integer, boolean); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_fetch(text, text, integer, boolean) RETURNS SETOF record
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_fetch';


ALTER FUNCTION public.dblink_fetch(text, text, integer, boolean) OWNER TO postgres;

--
-- TOC entry 54 (class 1255 OID 16477)
-- Dependencies: 3
-- Name: dblink_get_connections(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_get_connections() RETURNS text[]
    LANGUAGE c
    AS '$libdir/dblink', 'dblink_get_connections';


ALTER FUNCTION public.dblink_get_connections() OWNER TO postgres;

--
-- TOC entry 47 (class 1255 OID 16468)
-- Dependencies: 3 348
-- Name: dblink_get_pkey(text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_get_pkey(text) RETURNS SETOF dblink_pkey_results
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_get_pkey';


ALTER FUNCTION public.dblink_get_pkey(text) OWNER TO postgres;

--
-- TOC entry 52 (class 1255 OID 16475)
-- Dependencies: 3
-- Name: dblink_get_result(text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_get_result(text) RETURNS SETOF record
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_get_result';


ALTER FUNCTION public.dblink_get_result(text) OWNER TO postgres;

--
-- TOC entry 53 (class 1255 OID 16476)
-- Dependencies: 3
-- Name: dblink_get_result(text, boolean); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_get_result(text, boolean) RETURNS SETOF record
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_get_result';


ALTER FUNCTION public.dblink_get_result(text, boolean) OWNER TO postgres;

--
-- TOC entry 51 (class 1255 OID 16474)
-- Dependencies: 3
-- Name: dblink_is_busy(text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_is_busy(text) RETURNS integer
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_is_busy';


ALTER FUNCTION public.dblink_is_busy(text) OWNER TO postgres;

--
-- TOC entry 27 (class 1255 OID 16445)
-- Dependencies: 3
-- Name: dblink_open(text, text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_open(text, text) RETURNS text
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_open';


ALTER FUNCTION public.dblink_open(text, text) OWNER TO postgres;

--
-- TOC entry 28 (class 1255 OID 16446)
-- Dependencies: 3
-- Name: dblink_open(text, text, boolean); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_open(text, text, boolean) RETURNS text
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_open';


ALTER FUNCTION public.dblink_open(text, text, boolean) OWNER TO postgres;

--
-- TOC entry 29 (class 1255 OID 16447)
-- Dependencies: 3
-- Name: dblink_open(text, text, text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_open(text, text, text) RETURNS text
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_open';


ALTER FUNCTION public.dblink_open(text, text, text) OWNER TO postgres;

--
-- TOC entry 30 (class 1255 OID 16448)
-- Dependencies: 3
-- Name: dblink_open(text, text, text, boolean); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_open(text, text, text, boolean) RETURNS text
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_open';


ALTER FUNCTION public.dblink_open(text, text, text, boolean) OWNER TO postgres;

--
-- TOC entry 50 (class 1255 OID 16473)
-- Dependencies: 3
-- Name: dblink_send_query(text, text); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION dblink_send_query(text, text) RETURNS integer
    LANGUAGE c STRICT
    AS '$libdir/dblink', 'dblink_send_query';


ALTER FUNCTION public.dblink_send_query(text, text) OWNER TO postgres;

--
-- TOC entry 57 (class 1255 OID 16487)
-- Dependencies: 3 352
-- Name: setinstate(character varying, integer, bigint); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION setinstate(w character varying, ts integer, tid bigint) RETURNS void
    LANGUAGE plpgsql
    AS $_$
DECLARE word_state integer;
BEGIN
SELECT "Status" FROM "Words" WHERE "Word" = lower($1) INTO word_state;
IF word_state > -1 THEN
INSERT INTO "MindState" ("Word", "TScore", "TweetID") VALUES(lower($1), ts, tid);
END IF;
END;
$_$;


ALTER FUNCTION public.setinstate(w character varying, ts integer, tid bigint) OWNER TO postgres;

--
-- TOC entry 59 (class 1255 OID 16591)
-- Dependencies: 352 3
-- Name: setinstatecountry(character varying, integer, bigint, character varying); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION setinstatecountry(w character varying, ts integer, tid bigint, country character varying) RETURNS void
    LANGUAGE plpgsql
    AS $_$
DECLARE word_state integer;
BEGIN
SELECT "Status" FROM "Words" WHERE "Word" = lower($1) INTO word_state;
IF word_state > -1 THEN
INSERT INTO "MindState" ("Word", "TScore", "TweetID", "Country") VALUES(lower($1), ts, tid, country);
END IF;
END;
$_$;


ALTER FUNCTION public.setinstatecountry(w character varying, ts integer, tid bigint, country character varying) OWNER TO postgres;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 1541 (class 1259 OID 16395)
-- Dependencies: 1824 1825 1826 1827 1828 1829 1830 3
-- Name: MindState; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "MindState" (
    "MSID" integer NOT NULL,
    "Word" character varying(255) NOT NULL,
    "TScore" integer DEFAULT 0 NOT NULL,
    "InsertDate" timestamp with time zone DEFAULT now() NOT NULL,
    "TweetID" bigint DEFAULT 0 NOT NULL,
    "Country" text DEFAULT ''::text NOT NULL,
    "GPS_Long" double precision DEFAULT (-1) NOT NULL,
    "GPS_Lati" double precision DEFAULT (-1) NOT NULL,
    "GPS_Alti" double precision DEFAULT (-1) NOT NULL
);


ALTER TABLE public."MindState" OWNER TO postgres;

--
-- TOC entry 1540 (class 1259 OID 16393)
-- Dependencies: 1541 3
-- Name: MindState_MSID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "MindState_MSID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public."MindState_MSID_seq" OWNER TO postgres;

--
-- TOC entry 1849 (class 0 OID 0)
-- Dependencies: 1540
-- Name: MindState_MSID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "MindState_MSID_seq" OWNED BY "MindState"."MSID";


--
-- TOC entry 1539 (class 1259 OID 16385)
-- Dependencies: 1820 1821 1822 3
-- Name: Words; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "Words" (
    "Word" text NOT NULL,
    "Status" integer DEFAULT 0 NOT NULL,
    "InsertDate" timestamp with time zone DEFAULT now() NOT NULL,
    "Lang" character varying(20) DEFAULT ''::character varying NOT NULL
);


ALTER TABLE public."Words" OWNER TO postgres;

--
-- TOC entry 1823 (class 2604 OID 16398)
-- Dependencies: 1540 1541 1541
-- Name: MSID; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE "MindState" ALTER COLUMN "MSID" SET DEFAULT nextval('"MindState_MSID_seq"'::regclass);


--
-- TOC entry 1832 (class 2606 OID 16513)
-- Dependencies: 1539 1539
-- Name: PK_Words_Word; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "Words"
    ADD CONSTRAINT "PK_Words_Word" PRIMARY KEY ("Word");


--
-- TOC entry 1839 (class 2606 OID 16403)
-- Dependencies: 1541 1541
-- Name: pk_MindState_MSID; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "MindState"
    ADD CONSTRAINT "pk_MindState_MSID" PRIMARY KEY ("MSID");


--
-- TOC entry 1836 (class 1259 OID 16543)
-- Dependencies: 1541
-- Name: idx_MindState_InsertDate; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "idx_MindState_InsertDate" ON "MindState" USING btree ("InsertDate");


--
-- TOC entry 1837 (class 1259 OID 16542)
-- Dependencies: 1541
-- Name: idx_MindState_Word; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "idx_MindState_Word" ON "MindState" USING btree ("Word");


--
-- TOC entry 1833 (class 1259 OID 16541)
-- Dependencies: 1539
-- Name: idx_Words_Lang; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "idx_Words_Lang" ON "Words" USING btree ("Lang");


--
-- TOC entry 1834 (class 1259 OID 16540)
-- Dependencies: 1539
-- Name: idx_Words_Status; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX "idx_Words_Status" ON "Words" USING btree ("Status");


--
-- TOC entry 1835 (class 1259 OID 16539)
-- Dependencies: 1539
-- Name: idx_Words_Word; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE UNIQUE INDEX "idx_Words_Word" ON "Words" USING btree ("Word");


--
-- TOC entry 1844 (class 0 OID 0)
-- Dependencies: 3
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- TOC entry 1845 (class 0 OID 0)
-- Dependencies: 58
-- Name: checkinword(text); Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON FUNCTION checkinword(wxyz text) FROM PUBLIC;
REVOKE ALL ON FUNCTION checkinword(wxyz text) FROM postgres;
GRANT ALL ON FUNCTION checkinword(wxyz text) TO postgres;
GRANT ALL ON FUNCTION checkinword(wxyz text) TO PUBLIC;


--
-- TOC entry 1846 (class 0 OID 0)
-- Dependencies: 23
-- Name: dblink_connect_u(text); Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON FUNCTION dblink_connect_u(text) FROM PUBLIC;
REVOKE ALL ON FUNCTION dblink_connect_u(text) FROM postgres;
GRANT ALL ON FUNCTION dblink_connect_u(text) TO postgres;


--
-- TOC entry 1847 (class 0 OID 0)
-- Dependencies: 24
-- Name: dblink_connect_u(text, text); Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON FUNCTION dblink_connect_u(text, text) FROM PUBLIC;
REVOKE ALL ON FUNCTION dblink_connect_u(text, text) FROM postgres;
GRANT ALL ON FUNCTION dblink_connect_u(text, text) TO postgres;


--
-- TOC entry 1848 (class 0 OID 0)
-- Dependencies: 1541
-- Name: MindState; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE "MindState" FROM PUBLIC;
REVOKE ALL ON TABLE "MindState" FROM postgres;
GRANT ALL ON TABLE "MindState" TO postgres;
GRANT SELECT,INSERT ON TABLE "MindState" TO PUBLIC;


--
-- TOC entry 1850 (class 0 OID 0)
-- Dependencies: 1539
-- Name: Words; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE "Words" FROM PUBLIC;
REVOKE ALL ON TABLE "Words" FROM postgres;
GRANT ALL ON TABLE "Words" TO postgres;
GRANT ALL ON TABLE "Words" TO PUBLIC;


-- Completed on 2011-02-05 21:11:24 EST

--
-- PostgreSQL database dump complete
--


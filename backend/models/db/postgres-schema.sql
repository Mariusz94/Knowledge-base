CREATE TABLE public.article (
	"id" uuid NOT NULL,
	"title" varchar(255) NOT NULL,
	"content" varchar(255) NOT NULL,
	"like_count" float8 NULL,
	"dislike_count" float8 NULL,
    "author" varchar(255) NOT NULL,
	'created_at' timestamptz NOT NULL,
	'modified_at' timestamptz NOT NULL,
	CONSTRAINT article_pkey PRIMARY KEY (id)
);

CREATE TABLE public.comment (
	"id" uuid NOT NULL,
    "author" varchar(255) NOT NULL,
	"content" varchar(255) NOT NULL,
	"like_count" float8 NULL,
	"dislike_count" float8 NULL,
	"article_id" uuid NOT NULL,
	'created_at' timestamptz NOT NULL,
	'modified_at' timestamptz NOT NULL,
	CONSTRAINT comment_pkey PRIMARY KEY (id)
);

CREATE TABLE public.category (
	"id" uuid NOT NULL,
    "name" varchar(255) NOT NULL,
	'created_at' timestamptz NOT NULL,
	'modified_at' timestamptz NOT NULL,
	CONSTRAINT category_pkey PRIMARY KEY (id)
);

CREATE TABLE public.relation_category_article (
	"id" uuid NOT NULL,
	"category_id" uuid NOT NULL,
	"article_id" uuid NOT NULL,
	CONSTRAINT relation_category_article_pkey PRIMARY KEY (id),
    CONSTRAINT category_id_fk FOREIGN KEY (category_id) REFERENCES public.category(id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT article_id_fk FOREIGN KEY (article_id) REFERENCES public.article(id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE public.article (
	"id" uuid NOT NULL,
	"title" varchar(255) NOT NULL,
	"content" varchar(255) NOT NULL,
	"like_count" float8 NULL,
	"dislike_count" float8 NULL,
    "author" varchar(255) NOT NULL,
	"created_at" timestamptz NOT NULL,
	"modified_at" timestamptz NOT NULL,
	CONSTRAINT article_pkey PRIMARY KEY (id)
);

CREATE TABLE public.comment (
	"id" uuid NOT NULL,
    "author" varchar(255) NOT NULL,
	"content" varchar(255) NOT NULL,
	"like_count" float8 NULL,
	"dislike_count" float8 NULL,
	"article_id" uuid NOT NULL,
	"created_at" timestamptz NOT NULL,
	"modified_at" timestamptz NOT NULL,
	CONSTRAINT comment_pkey PRIMARY KEY (id)
);

CREATE TABLE public.category (
	"id" uuid NOT NULL,
    "name" varchar(255) NOT NULL,
	"created_at" timestamptz NOT NULL,
	"modified_at" timestamptz NOT NULL,
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

INSERT INTO public.article (id,title,content,like_count,dislike_count,author,created_at,modified_at)
VALUES ('9650f87d-c6cc-4830-ad9a-d7c2d8bef522', 'Python','Pobieranie aktualnego czas, data, timestamp import pandas as pd -> pd.Timestamp.now() int(pd.Timestamp.now().value /10**9) -> 139397478',0,0,'mlyszczarz','2022-06-07T22:59:00+01','2022-06-07T23:59:00+01');

INSERT INTO public.article (id,title,content,like_count,dislike_count,author,created_at,modified_at)
VALUES ('b38c7e20-e688-11ec-8fea-0242ac120002', 'Venv','Tworzenie odrębnego środowiska\npython -m venv venv\n. venv\"Scripts\"activate\ndeactivate\nTworzenie venv z bibliotekami w systemie\npython -m venv --system-site-packages venv\n. venv\"Scripts\"activate\nPobieranie zależności do pliku tekstowego\npip freeze > zaleznosci.txt',0,0,'mlyszczarz','2022-06-06T22:59:00+01','2022-06-06T23:59:00+01');

INSERT INTO public.article (id,title,content,like_count,dislike_count,author,created_at,modified_at)
VALUES ('cae6eeee-e68d-11ec-8fea-0242ac120002', 'Dockerfile','FROM <OBRAZ> - jest to komenda, którą będą się zawsze zaczynały pliki Dockerfile. Wskazujemy nią obraz bazowy, jaki chcemy modyfikować, by stworzyć własny. \nWORKDIR <PATH> - komenda służy do przejścia do konkretnego katalogu wewnątrz kontenera Dockera. Wszystkie nasze kolejne operacje będą wykonywane właśnie w tym wskazanym katalogu. W przypadku braku odpowiedniego katalogu zostanie on utworzony. \nCOPY <SRC> <DEST> - jest komendą wykorzystywaną do kopiowania plików z komputera do tworzonego obrazu. Wykorzystujemy ją np. do kopiowania plików źródłowych naszej aplikacji. \nADD <SRC> <DEST> - jest komendą podobną do COPY. Za jej pomocą także możemy kopiować pliki z komputera, do obrazu. Jednakże jako argument <SRC> nie musimy podać pliku z naszego komputera. W jego miejscu możemy podać na przykład URL, a podczas budowy obrazu Docker pobierze zasoby spod podanego linku. Ponadto, jeśli przez argument <SRC> przekażemy skompresowany plik, zostanie on rozpakowany. \nEXPOSE <port>[/<protokół>] - otwiera port sieciowy kontenera, który umożliwia nawiązanie komunikacji pomiędzy kontenerem a światem zewnętrznym (domyślny protokół TCP, ale może być też UDP) // EXPOSE 7373/udp 8080 \nRUN <COMMAND> - służy do uruchamiania komend shella wewnątrz kontenera Dockera w trakcie budowy obrazu (drugi sposób to tablica exec) . \n',0,0,'wnowak','2022-05-07T22:59:00+01','2022-05-07T23:59:00+01');

INSERT INTO public.category (id,"name",created_at,modified_at)
VALUES ('43b4474e-ffe6-4156-b0c3-452df5dba2fc', 'Python','2022-06-07T22:59:00+01','2022-06-07T23:59:00+01')

INSERT INTO public.category (id,"name",created_at,modified_at)
VALUES ('56b4474e-ffe6-4156-b0c3-452df5dba2fc', 'Docker','2022-06-07T22:59:00+01','2022-06-07T23:59:00+01')

INSERT INTO public.comment (id,author,content,like_count,dislike_count,article_id,created_at,modified_at)
VALUES ('90b4474e-ffe6-4156-b0c3-452df5dba2fc', 'wnowak','Super pomocny artykul',0,0,'b38c7e20-e688-11ec-8fea-0242ac120002','2022-06-07T23:59:00+01','2022-06-07T23:59:00+01')

INSERT INTO public.comment (id,author,content,like_count,dislike_count,article_id,created_at,modified_at)
VALUES ('54g4474e-ffe6-4156-b0c3-452df5dba2fc', 'wnowak','Super pomocny artykul v2',0,0,'b38c7e20-e688-11ec-8fea-0242ac120002','2022-06-07T23:59:00+01','2022-06-07T23:59:00+01')

INSERT INTO public.relation_category_article (id,category_id,article_id)
VALUES ('87b4474e-ffe6-4156-b0c3-452df5dba2fc', '56b4474e-ffe6-4156-b0c3-452df5dba2fc','cae6eeee-e68d-11ec-8fea-0242ac120002')

INSERT INTO public.relation_category_article (id,category_id,article_id)
VALUES ('99b4474e-ffe6-4156-b0c3-452df5dba2fc', '43b4474e-ffe6-4156-b0c3-452df5dba2fc','9650f87d-c6cc-4830-ad9a-d7c2d8bef522')

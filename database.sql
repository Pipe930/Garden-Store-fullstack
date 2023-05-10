

CREATE TABLE USER(
    id_user INT(10) NOT NULL,
    first_name VARCHAR(20) NULL,
    last_name VARCHAR(20) NULL,
    username VARCHAR(40) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(16) NOT NULL,
    last_login DATE NOT NULL,
    is_staff CHAR(1) NOT NULL,
    is_superuser CHAR(1) NOT NULL,
    date_joined DATE NOT NULL,

    CONSTRAINT pk_id_user PRIMARY KEY (id_user)
);

ALTER TABLE USER MODIFY id_user INT(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT = 1;

CREATE TABLE SUBSCRIPTION(
    id_subsciption INT(10) NOT NULL,
    username VARCHAR(40) NOT NULL,
    email VARCHAR(100) NOT NULL,
    amount INT(6) NOT NULL,
    id_user INT(10) NOT NULL,

    CONSTRAINT pk_id_subsciption PRIMARY KEY (id_subsciption),
    CONSTRAINT fk_id_user FOREIGN KEY (id_user) REFERENCES USER(id_user)
);

ALTER TABLE SUBSCRIPTION MODIFY id_subsciption INT(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT = 1;

CREATE TABLE CART(
    id_cart INT(10) NOT NULL,
    created timestamp NOT NULL DEFAULT current_timestamp,
    total_price INT(10) NOT NULL,
    id_user INT(10) NOT NULL,

    CONSTRAINT pk_id_cart PRIMARY KEY (id_cart),
    CONSTRAINT fk_id_user FOREIGN KEY (id_user) REFERENCES USER(id_user)
);

ALTER TABLE CART MODIFY id_cart INT(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT = 1;

CREATE TABLE CATEGORY(
    id_category INT(10) NOT NULL,
    name VARCHAR(10) NOT NULL,
    description VARCHAR(255) NULL,

    CONSTRAINT pk_id_category PRIMARY KEY (id_category)
);

ALTER TABLE CATEGORY MODIFY id_category INT(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT = 1;

CREATE TABLE OFFER(
    id_offer INT(10) NOT NULL,
    name VARCHAR(40) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    discount INT(3) NOT NULL,

    CONSTRAINT pk_id_offer PRIMARY KEY (id_offer)
);

ALTER TABLE OFFER MODIFY id_offer INT(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT = 1;

CREATE TABLE PRODUCT(
    id_prodruct INT(10) NOT NULL,
    name_product VARCHAR(40) NOT NULL,
    price INT(10) NOT NULL,
    stock INT(5) NOT NULL,
    image BLOB NOT NULL,
    description TEXT,
    slug VARCHAR(255) NOT NULL,
    condition CHAR(1) NOT NULL,
    created timestamp NOT NULL DEFAULT current_timestamp,
    id_category INT(10) NOT NULL,
    id_offer INT(10) NOT NULL,

    CONSTRAINT pk_id_prodruct PRIMARY KEY (id_prodruct),
    CONSTRAINT fk_id_category FOREIGN KEY (id_category) REFERENCES CATEGORY(id_category),
    CONSTRAINT fk_id_offer FOREIGN KEY (id_offer) REFERENCES CATEGORY(id_offer)
);

ALTER TABLE PRODUCT MODIFY id_prodruct INT(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT = 1;

CREATE TABLE ITEMS(
    id_items INT(20) NOT NULL,
    price INT(10) NOT NULL,
    quantity INT(6) NOT NULL,
    id_cart INT(10) NOT NULL,
    id_product INT(10) NOT NULL,

    CONSTRAINT pk_id_items PRIMARY KEY (id_items),
    CONSTRAINT fk_id_cart FOREIGN KEY (id_cart) REFERENCES CART(id_cart),
    CONSTRAINT fk_id_product FOREIGN KEY (id_product) REFERENCES PRODUCT(id_product)
);

ALTER TABLE ITEMS MODIFY id_items INT(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT = 1;

CREATE TABLE VOUCHER(
    id_voucher INT(10) NOT NULL,
    code VARCHAR(32) NOT NULL,
    created timestamp NOT NULL DEFAULT current_timestamp,
    total_price INT(10) NOT NULL,
    id_cart INT(10) NOT NULL,
    id_user INT(10) NOT NULL,

    CONSTRAINT pk_id_voucher PRIMARY KEY (id_voucher),
    CONSTRAINT fk_id_cart FOREIGN KEY (id_cart) REFERENCES CART(id_cart),
    CONSTRAINT fk_id_user FOREIGN KEY (id_user) REFERENCES USER(id_user)
);

ALTER TABLE VOUCHER MODIFY id_voucher INT(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT = 1;

CREATE TABLE REGION(
    id_region INT(10) NOT NULL,
    name VARCHAR(40) NOT NULL,
    initials VARCHAR(6) NOT NULL,

    CONSTRAINT pk_id_region PRIMARY KEY (id_region)
);

ALTER TABLE REGION MODIFY id_region INT(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT = 1;

CREATE TABLE PROVINCE(
    id_province INT(10) NOT NULL,
    name INT(10) NOT NULL,
    id_region INT(10) NOT NULL,

    CONSTRAINT pk_id_province PRIMARY KEY (id_province),
    CONSTRAINT fk_id_region FOREIGN KEY (id_region) REFERENCES REGION(id_region)
);

ALTER TABLE PROVINCE MODIFY id_province INT(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT = 1;

CREATE TABLE COMMUNE(
    id_commune INT(10) NOT NULL,
    name VARCHAR(40) NOT NULL,
    id_province INT(10) NOT NULL,

    CONSTRAINT pk_id_commune PRIMARY KEY (id_commune),
    CONSTRAINT fk_id_province FOREIGN KEY (id_province) REFERENCES PROVINCE(id_province)
);

ALTER TABLE COMMUNE MODIFY id_commune INT(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT = 1;

CREATE TABLE ORDER(
    id_order INT(10) NOT NULL,
    code VARCHAR(32) NOT NULL,
    created timestamp NOT NULL DEFAULT current_timestamp,
    condition VARCHAR(20) NOT NULL,
    withdrawal VARCHAR(20) NOT NULL,
    direction VARCHAR(100) NOT NULL,
    num_department INT(10) NULL,
    id_commune INT(10) NOT NULL,
    id_voucher INT(10) NOT NULL,
    id_user INT(10) NOT NULL,

    CONSTRAINT pk_id_order PRIMARY KEY (id_order),
    CONSTRAINT fk_id_commune FOREIGN KEY (id_commune) REFERENCES COMMUNE(id_commune),
    CONSTRAINT fk_id_voucher FOREIGN KEY (id_voucher) REFERENCES VOUVHER(id_voucher),
    CONSTRAINT fk_id_user FOREIGN KEY (id_user) REFERENCES USER(id_user)
);

ALTER TABLE ORDER MODIFY id_order INT(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT = 1;

-- Regiones de Chile

INSERT INTO regions VALUES(1, "Region de Arica y Parinacota", "XV");
INSERT INTO regions VALUES(2, "Region de Tarapaca", "I");
INSERT INTO regions VALUES(3, "Region de Antofagasta", "II");
INSERT INTO regions VALUES(4, "Region de Atacama", "III");
INSERT INTO regions VALUES(5, "Region de Coquimbo", "IV");
INSERT INTO regions VALUES(6, "Region de Valparaíso", "V");
INSERT INTO regions VALUES(7, "Region del Libertador General Bernardo O'Higgins", "VI");
INSERT INTO regions VALUES(8, "Region del Maule", "VII");
INSERT INTO regions VALUES(9, "Region de Ñuble", "XVI");
INSERT INTO regions VALUES(10, "Region del Biobio", "VIII");
INSERT INTO regions VALUES(11, "Región de La Araucania", "IX");
INSERT INTO regions VALUES(12, "Region de Los Rios", "XIV");
INSERT INTO regions VALUES(13, "Region de Los Lagos", "X");
INSERT INTO regions VALUES(14, "Region de Aysen del General Carlos Ibañez del Campo", "XI");
INSERT INTO regions VALUES(15, "Region de Magallanes y de la Antartica Chilena ", "XII");
INSERT INTO regions VALUES(16, "Region de Metropolitana de Santiago", "");

-- Provincias de Chile

INSERT INTO provinces VALUES(1, "Provincia de Arica", 1);
INSERT INTO provinces VALUES(2, "Provincia de Parinacota", 1);

INSERT INTO provinces VALUES(3, "Provincia de Iquique", 2);
INSERT INTO provinces VALUES(4, "Provincia del Tamarugal", 2);

INSERT INTO provinces VALUES(5, "Provincia de Tocopilla", 3);
INSERT INTO provinces VALUES(6, "Provincia de El Loa", 3);
INSERT INTO provinces VALUES(7, "Provincia de Antofagasta", 3);

INSERT INTO provinces VALUES(8, "Provincia de Chañaral", 4);
INSERT INTO provinces VALUES(9, "Provincia de Copiapo", 4);
INSERT INTO provinces VALUES(10, "Provincia de Huasco", 4);

INSERT INTO provinces VALUES(11, "Provincia de Elqui", 5);
INSERT INTO provinces VALUES(12, "Provincia de Limari", 5);
INSERT INTO provinces VALUES(13, "Provincia de Choapa", 5);

INSERT INTO provinces VALUES(14, "Provincia de Petorca", 6);
INSERT INTO provinces VALUES(15, "Provincia de Los Andes", 6);
INSERT INTO provinces VALUES(16, "Provincia de San Felipe de Aconcagua", 6);
INSERT INTO provinces VALUES(17, "Provincia de Quillota", 6);
INSERT INTO provinces VALUES(18, "Provincia de Valparaiso", 6);
INSERT INTO provinces VALUES(19, "Provincia de San Antonio", 6);
INSERT INTO provinces VALUES(20, "Provincia de Isla de Pascua", 6);
INSERT INTO provinces VALUES(21, "Provincia de Marga Marga", 6);

INSERT INTO provinces VALUES(22, "Provincia de Chacabuco", 16);
INSERT INTO provinces VALUES(23, "Provincia de Santiago", 16);
INSERT INTO provinces VALUES(24, "Provincia de Cordillera", 16);
INSERT INTO provinces VALUES(25, "Provincia de Maipo", 16);
INSERT INTO provinces VALUES(26, "Provincia de Melipilla", 16);
INSERT INTO provinces VALUES(27, "Provincia de Talagante", 16);

INSERT INTO provinces VALUES(28, "Provincia de Cachapoal", 7);
INSERT INTO provinces VALUES(29, "Provincia de Colchagua", 7);
INSERT INTO provinces VALUES(30, "Provincia Cardenal Caro", 7);

INSERT INTO provinces VALUES(31, "Provincia de Curico", 8);
INSERT INTO provinces VALUES(32, "Provincia de Talca", 8);
INSERT INTO provinces VALUES(33, "Provincia de Linares", 8);
INSERT INTO provinces VALUES(34, "Provincia de Cauquenes", 8);

INSERT INTO provinces VALUES(35, "Provincia de Diguillin", 9);
INSERT INTO provinces VALUES(36, "Provincia de Itata", 9);
INSERT INTO provinces VALUES(37, "Provincia de Punilla", 9);

INSERT INTO provinces VALUES(38, "Provincia de Biobio", 10);
INSERT INTO provinces VALUES(39, "Provincia de Concepcion", 10);
INSERT INTO provinces VALUES(40, "Provincia de Arauco", 10);

INSERT INTO provinces VALUES(41, "Provincia de Malleco", 11);
INSERT INTO provinces VALUES(42, "Provincia de Cautin", 11);

INSERT INTO provinces VALUES(43, "Provincia de Valdivia", 12);
INSERT INTO provinces VALUES(44, "Provincia del Ranco", 12);

INSERT INTO provinces VALUES(45, "Provincia de Osorno", 13);
INSERT INTO provinces VALUES(46, "Provincia de Llanquihue", 13);
INSERT INTO provinces VALUES(47, "Provincia de Chiloe", 13);
INSERT INTO provinces VALUES(48, "Provincia de Palena", 13);

INSERT INTO provinces VALUES(49, "Provincia de Coyhaique", 14);
INSERT INTO provinces VALUES(50, "Provincia de Aysen", 14);
INSERT INTO provinces VALUES(51, "Provincia General Carrera", 14);
INSERT INTO provinces VALUES(52, "Provincia Capitan Prat", 14);

INSERT INTO provinces VALUES(53, "Provincia de Ultima Esperanza", 15);
INSERT INTO provinces VALUES(54, "Provincia de Magallanes", 15);
INSERT INTO provinces VALUES(55, "Provincia de Tierra del Fuego", 15);
INSERT INTO provinces VALUES(56, "Provincia Antartica Chilena", 15);

-- Comunas de Chile

INSERT INTO communes VALUES(1, "Arica", 1);
INSERT INTO communes VALUES(2, "Camarones", 1);

INSERT INTO communes VALUES(3, "General Lagos", 2);
INSERT INTO communes VALUES(4, "Putre", 2);

INSERT INTO communes VALUES(5, "Alto Hospicio", 3);
INSERT INTO communes VALUES(6, "Iquique", 3);

INSERT INTO communes VALUES(7, "Camiña", 4);
INSERT INTO communes VALUES(8, "Colchane", 4);
INSERT INTO communes VALUES(9, "Huara", 4);
INSERT INTO communes VALUES(10, "Pica", 4);
INSERT INTO communes VALUES(11, "Pozo Almonte", 4);

INSERT INTO communes VALUES(12, "Antofagasta", 7);
INSERT INTO communes VALUES(13, "Mejillones", 7);
INSERT INTO communes VALUES(14, "Sierra Gorda", 7);
INSERT INTO communes VALUES(15, "Taltal", 7);

INSERT INTO communes VALUES(16, "Calama", 6);
INSERT INTO communes VALUES(17, "Ollagüe", 6);
INSERT INTO communes VALUES(18, "San Pedro de Atacama", 6);

INSERT INTO communes VALUES(19, "Maria Elena", 5);
INSERT INTO communes VALUES(20, "Tocopilla", 5);

INSERT INTO communes VALUES(21, "Chañaral", 8);
INSERT INTO communes VALUES(22, "Diego de Almagro", 8);

INSERT INTO communes VALUES(23, "Caldera", 9);
INSERT INTO communes VALUES(24, "Copiapo", 9);
INSERT INTO communes VALUES(25, "Tierra Amarilla", 9);

INSERT INTO communes VALUES(26, "Alto del Carmen", 10);
INSERT INTO communes VALUES(27, "Freirina", 10);
INSERT INTO communes VALUES(28, "Huasco", 10);
INSERT INTO communes VALUES(29, "Vallenar", 10);

INSERT INTO communes VALUES(30, "Andacollo", 11);
INSERT INTO communes VALUES(31, "Coquimbo", 11);
INSERT INTO communes VALUES(32, "La Higuera", 11);
INSERT INTO communes VALUES(33, "La Serena", 11);
INSERT INTO communes VALUES(34, "Paihuano", 11);
INSERT INTO communes VALUES(35, "Vicuña", 11);

INSERT INTO communes VALUES(36, "Combarbala", 12);
INSERT INTO communes VALUES(37, "Monte Patria", 12);
INSERT INTO communes VALUES(38, "Ovalle", 12);
INSERT INTO communes VALUES(39, "Punitaqui", 12);
INSERT INTO communes VALUES(40, "Rio Hurtado", 12);

INSERT INTO communes VALUES(41, "Canela", 13);
INSERT INTO communes VALUES(42, "Illapel", 13);
INSERT INTO communes VALUES(43, "Los Vilos", 13);
INSERT INTO communes VALUES(44, "Salamanca", 13);

INSERT INTO communes VALUES(45, "Calle Larga", 15);
INSERT INTO communes VALUES(46, "Los Andes", 15);
INSERT INTO communes VALUES(47, "San Esteban", 15);
INSERT INTO communes VALUES(48, "Rinconada", 15);

INSERT INTO communes VALUES(49, "Cabildo", 14);
INSERT INTO communes VALUES(50, "La Ligua", 14);
INSERT INTO communes VALUES(51, "Papudo", 14);
INSERT INTO communes VALUES(52, "Petorca", 14);
INSERT INTO communes VALUES(53, "Zapallar", 14);

INSERT INTO communes VALUES(54, "Hijuelas", 17);
INSERT INTO communes VALUES(55, "La Calera", 17);
INSERT INTO communes VALUES(56, "La Cruz", 17);
INSERT INTO communes VALUES(57, "Nogales", 17);
INSERT INTO communes VALUES(58, "Quillota", 17);

INSERT INTO communes VALUES(59, "Algarrobo", 19);
INSERT INTO communes VALUES(60, "Cartagena", 19);
INSERT INTO communes VALUES(61, "El Quisco", 19);
INSERT INTO communes VALUES(62, "El Tabo", 19);
INSERT INTO communes VALUES(63, "San Antonio", 19);
INSERT INTO communes VALUES(64, "Santo Domingo", 19);

INSERT INTO communes VALUES(65, "Catemu", 16);
INSERT INTO communes VALUES(66, "Llay-Llay", 16);
INSERT INTO communes VALUES(67, "Panquehue", 16);
INSERT INTO communes VALUES(68, "Putaendo", 16);
INSERT INTO communes VALUES(69, "San Felipe", 16);
INSERT INTO communes VALUES(70, "Santa Maria", 16);

INSERT INTO communes VALUES(71, "Viña del Mar", 18);
INSERT INTO communes VALUES(72, "Valparaiso", 18);
INSERT INTO communes VALUES(73, "Quintero", 18);
INSERT INTO communes VALUES(74, "Puchuncavi", 18);
INSERT INTO communes VALUES(75, "Juan Fernandez", 18);
INSERT INTO communes VALUES(76, "Concon", 18);
INSERT INTO communes VALUES(77, "Casablanca", 18);

INSERT INTO communes VALUES(78, "Villa Alemana", 21);
INSERT INTO communes VALUES(79, "Quilpue", 21);
INSERT INTO communes VALUES(80, "Olmue", 21);
INSERT INTO communes VALUES(81, "Limache", 21);

INSERT INTO communes VALUES(82, "Rapa Nui", 20);

INSERT INTO communes VALUES(83, "Colina", 22);
INSERT INTO communes VALUES(84, "Til Til", 22);
INSERT INTO communes VALUES(85, "Lampa", 22);

INSERT INTO communes VALUES(86, "San Jose de Maipo", 24);
INSERT INTO communes VALUES(87, "Puente Alto", 24);
INSERT INTO communes VALUES(88, "Pirque", 24);

INSERT INTO communes VALUES(89, "Calera de Tango", 25);
INSERT INTO communes VALUES(90, "San Bernardo", 25);
INSERT INTO communes VALUES(91, "Buin", 25);
INSERT INTO communes VALUES(92, "Paine", 25);

INSERT INTO communes VALUES(93, "Alhue", 26);
INSERT INTO communes VALUES(94, "San Pedro", 26);
INSERT INTO communes VALUES(95, "Melipilla", 26);
INSERT INTO communes VALUES(96, "Maria Pinto", 26);
INSERT INTO communes VALUES(97, "Curacavi", 26);

INSERT INTO communes VALUES(98, "Cerrillos", 23);
INSERT INTO communes VALUES(99, "Cerro Navia", 23);
INSERT INTO communes VALUES(100, "Conchali", 23);
INSERT INTO communes VALUES(101, "El Bosque", 23);
INSERT INTO communes VALUES(102, "Estacion Central", 23);
INSERT INTO communes VALUES(103, "Huechuraba", 23);
INSERT INTO communes VALUES(104, "Independencia", 23);
INSERT INTO communes VALUES(105, "La Cisterna", 23);
INSERT INTO communes VALUES(106, "La Granja", 23);
INSERT INTO communes VALUES(107, "La Florida", 23);
INSERT INTO communes VALUES(108, "La Pintana", 23);
INSERT INTO communes VALUES(109, "La Reina", 23);
INSERT INTO communes VALUES(110, "Las Condes", 23);
INSERT INTO communes VALUES(111, "Lo Barnechea", 23);
INSERT INTO communes VALUES(112, "Lo Espejo", 23);
INSERT INTO communes VALUES(113, "Lo Prado", 23);
INSERT INTO communes VALUES(114, "Macul", 23);
INSERT INTO communes VALUES(115, "Maipu", 23);
INSERT INTO communes VALUES(116, "Ñuñoa", 23);
INSERT INTO communes VALUES(117, "Pedro Aguirre Cerda", 23);
INSERT INTO communes VALUES(118, "Peñalolen", 23);
INSERT INTO communes VALUES(119, "Providencia", 23);
INSERT INTO communes VALUES(120, "Pudahuel", 23);
INSERT INTO communes VALUES(121, "Quilicura", 23);
INSERT INTO communes VALUES(122, "Quinta Normal", 23);
INSERT INTO communes VALUES(123, "Recoleta", 23);
INSERT INTO communes VALUES(124, "Renca", 23);
INSERT INTO communes VALUES(125, "San Miguel", 23);
INSERT INTO communes VALUES(126, "San Joaquin", 23);
INSERT INTO communes VALUES(127, "San Ramon", 23);
INSERT INTO communes VALUES(128, "Santiago", 23);
INSERT INTO communes VALUES(129, "Vitacura", 23);

INSERT INTO communes VALUES(130, "El Monte", 27);
INSERT INTO communes VALUES(131, "Isla de Maipo", 27);
INSERT INTO communes VALUES(132, "Padre Hurtado", 27);
INSERT INTO communes VALUES(133, "Peñaflor", 27);
INSERT INTO communes VALUES(134, "Talagante", 27);

INSERT INTO communes VALUES(135, "Codegua", 28);
INSERT INTO communes VALUES(136, "Coinco", 28);
INSERT INTO communes VALUES(137, "Coltauco", 28);
INSERT INTO communes VALUES(138, "Doñihue", 28);
INSERT INTO communes VALUES(139, "Graneros", 28);
INSERT INTO communes VALUES(140, "Las Cabras", 28);
INSERT INTO communes VALUES(141, "Machali", 28);
INSERT INTO communes VALUES(142, "Malloa", 28);
INSERT INTO communes VALUES(143, "Mostazal", 28);
INSERT INTO communes VALUES(144, "Olivar", 28);
INSERT INTO communes VALUES(145, "Peumo", 28);
INSERT INTO communes VALUES(146, "Pichidegua", 28);
INSERT INTO communes VALUES(147, "Quinta de Tilcoco", 28);
INSERT INTO communes VALUES(148, "Rancagua", 28);
INSERT INTO communes VALUES(149, "Rengo", 28);
INSERT INTO communes VALUES(150, "Requinoa", 28);
INSERT INTO communes VALUES(151, "San Vicente de Tagua Tagua", 28);

INSERT INTO communes VALUES(152, "La Estrella", 30);
INSERT INTO communes VALUES(153, "Litueche", 30);
INSERT INTO communes VALUES(154, "Marchigüe", 30);
INSERT INTO communes VALUES(155, "Navidad", 30);
INSERT INTO communes VALUES(156, "Paredones", 30);
INSERT INTO communes VALUES(157, "Pichilemu", 30);

INSERT INTO communes VALUES(158, "Chepica", 29);
INSERT INTO communes VALUES(159, "Chimbarongo", 29);
INSERT INTO communes VALUES(160, "Lolol", 29);
INSERT INTO communes VALUES(161, "Nancagua", 29);
INSERT INTO communes VALUES(162, "Palmilla", 29);
INSERT INTO communes VALUES(163, "Peralillo", 29);
INSERT INTO communes VALUES(164, "Placilla", 29);
INSERT INTO communes VALUES(165, "Pumanque", 29);
INSERT INTO communes VALUES(166, "San Fernando", 29);
INSERT INTO communes VALUES(167, "Santa Cruz", 29);

INSERT INTO communes VALUES(168, "Cauquenes", 34);
INSERT INTO communes VALUES(169, "Chanco", 34);
INSERT INTO communes VALUES(170, "Pelluhue", 34);

INSERT INTO communes VALUES(171, "Curico", 31);
INSERT INTO communes VALUES(172, "Hualañe", 31);
INSERT INTO communes VALUES(173, "Licanten", 31);
INSERT INTO communes VALUES(174, "Molina", 31);
INSERT INTO communes VALUES(175, "Rauco", 31);
INSERT INTO communes VALUES(176, "Romeral", 31);
INSERT INTO communes VALUES(177, "Sagrada Familia", 31);
INSERT INTO communes VALUES(178, "Teno", 31);
INSERT INTO communes VALUES(179, "Vichuquen", 31);

INSERT INTO communes VALUES(180, "Colbun", 33);
INSERT INTO communes VALUES(181, "Linares", 33);
INSERT INTO communes VALUES(182, "Longavi", 33);
INSERT INTO communes VALUES(183, "Parral", 33);
INSERT INTO communes VALUES(184, "Retiro", 33);
INSERT INTO communes VALUES(185, "San Javier", 33);
INSERT INTO communes VALUES(186, "Villa Alegre", 33);
INSERT INTO communes VALUES(187, "Yerbas Buenas", 33);

INSERT INTO communes VALUES(188, "Constitucion", 32);
INSERT INTO communes VALUES(189, "Curepto", 32);
INSERT INTO communes VALUES(190, "Empedrado", 32);
INSERT INTO communes VALUES(191, "Maule", 32);
INSERT INTO communes VALUES(192, "Pelarco", 32);
INSERT INTO communes VALUES(193, "Pencahue", 32);
INSERT INTO communes VALUES(194, "Rio Claro", 32);
INSERT INTO communes VALUES(195, "San Clemente", 32);
INSERT INTO communes VALUES(196, "San Rafael", 32);
INSERT INTO communes VALUES(197, "Talca", 32);

INSERT INTO communes VALUES(198, "Cobquecura", 36);
INSERT INTO communes VALUES(199, "Coelemu", 36);
INSERT INTO communes VALUES(200, "Ninhue", 36);
INSERT INTO communes VALUES(201, "Portezuelo", 36);
INSERT INTO communes VALUES(202, "Quirihue", 36);
INSERT INTO communes VALUES(203, "Ranquil", 36);
INSERT INTO communes VALUES(204, "Trehuaco", 36);

INSERT INTO communes VALUES(205, "Bulnes", 35);
INSERT INTO communes VALUES(206, "Chillan Viejo", 35);
INSERT INTO communes VALUES(207, "Chillan", 35);
INSERT INTO communes VALUES(208, "El Carmen", 35);
INSERT INTO communes VALUES(209, "Pemuco", 35);
INSERT INTO communes VALUES(210, "Quillon", 35);
INSERT INTO communes VALUES(211, "Pinto", 35);
INSERT INTO communes VALUES(212, "San Ignacio", 35);
INSERT INTO communes VALUES(213, "Yungay", 35);

INSERT INTO communes VALUES(214, "San Nicolas", 37);
INSERT INTO communes VALUES(215, "San Fabian", 37);
INSERT INTO communes VALUES(216, "San Carlos", 37);
INSERT INTO communes VALUES(217, "Ñiquen", 37);
INSERT INTO communes VALUES(218, "Coihueco", 37);

INSERT INTO communes VALUES(219, "Arauco", 40);
INSERT INTO communes VALUES(220, "Cañete", 40);
INSERT INTO communes VALUES(221, "Contulmo", 40);
INSERT INTO communes VALUES(222, "Curanilahue", 40);
INSERT INTO communes VALUES(223, "Lebu", 40);
INSERT INTO communes VALUES(224, "Los Alamos", 40);
INSERT INTO communes VALUES(225, "Tirua", 40);

INSERT INTO communes VALUES(226, "Alto Biobio", 38);
INSERT INTO communes VALUES(227, "Antuco", 38);
INSERT INTO communes VALUES(228, "Cabrero", 38);
INSERT INTO communes VALUES(229, "Laja", 38);
INSERT INTO communes VALUES(230, "Los Angeles", 38);
INSERT INTO communes VALUES(231, "Mulchen", 38);
INSERT INTO communes VALUES(232, "Nacimiento", 38);
INSERT INTO communes VALUES(233, "Negrete", 38);
INSERT INTO communes VALUES(234, "Quilaco", 38);
INSERT INTO communes VALUES(235, "Quilleco", 38);
INSERT INTO communes VALUES(236, "San Rosendo", 38);
INSERT INTO communes VALUES(237, "Santa Barbara", 38);
INSERT INTO communes VALUES(238, "Tucapel", 38);
INSERT INTO communes VALUES(239, "Yumbel", 38);

INSERT INTO communes VALUES(240, "Chiguayante", 39);
INSERT INTO communes VALUES(241, "Concepcion", 39);
INSERT INTO communes VALUES(242, "Coronel", 39);
INSERT INTO communes VALUES(243, "Florida", 39);
INSERT INTO communes VALUES(244, "Hualpen", 39);
INSERT INTO communes VALUES(245, "Hualqui", 39);
INSERT INTO communes VALUES(246, "Lota", 39);
INSERT INTO communes VALUES(247, "Penco", 39);
INSERT INTO communes VALUES(248, "San Pedro de la Paz", 39);
INSERT INTO communes VALUES(249, "Santa Juana", 39);
INSERT INTO communes VALUES(250, "Talcahuano", 39);
INSERT INTO communes VALUES(251, "Tome", 39);

INSERT INTO communes VALUES(252, "Carahue", 42);
INSERT INTO communes VALUES(253, "Cholchol", 42);
INSERT INTO communes VALUES(254, "Cunco", 42);
INSERT INTO communes VALUES(255, "Curarrehue", 42);
INSERT INTO communes VALUES(256, "Freire", 42);
INSERT INTO communes VALUES(257, "Galvarino", 42);
INSERT INTO communes VALUES(258, "Gorbea", 42);
INSERT INTO communes VALUES(259, "Lautaro", 42);
INSERT INTO communes VALUES(260, "Loncoche", 42);
INSERT INTO communes VALUES(261, "Melipeuco", 42);
INSERT INTO communes VALUES(262, "Nueva Imperial", 42);
INSERT INTO communes VALUES(263, "Padre Las Casas", 42);
INSERT INTO communes VALUES(264, "Perquenco", 42);
INSERT INTO communes VALUES(265, "Pitrufquén", 42);
INSERT INTO communes VALUES(266, "Pucon", 42);
INSERT INTO communes VALUES(267, "Puerto Saavedra", 42);
INSERT INTO communes VALUES(268, "Temuco", 42);
INSERT INTO communes VALUES(269, "Teodoro Schmidt", 42);
INSERT INTO communes VALUES(270, "Tolten", 42);
INSERT INTO communes VALUES(271, "Vilcun", 42);
INSERT INTO communes VALUES(272, "Villarrica", 42);

INSERT INTO communes VALUES(273, "Angol", 41);
INSERT INTO communes VALUES(274, "Collipulli", 41);
INSERT INTO communes VALUES(275, "Curacautín", 41);
INSERT INTO communes VALUES(276, "Ercilla", 41);
INSERT INTO communes VALUES(277, "Lonquimay", 41);
INSERT INTO communes VALUES(278, "Los Sauces", 41);
INSERT INTO communes VALUES(279, "Lumaco", 41);
INSERT INTO communes VALUES(280, "Puren", 41);
INSERT INTO communes VALUES(281, "Renaico", 41);
INSERT INTO communes VALUES(282, "Traiguén", 41);
INSERT INTO communes VALUES(283, "Victoria", 41);

INSERT INTO communes VALUES(284, "Mariquina", 43);
INSERT INTO communes VALUES(285, "Lanco", 43);
INSERT INTO communes VALUES(286, "Mafil", 43);
INSERT INTO communes VALUES(287, "Valdivia", 43);
INSERT INTO communes VALUES(288, "Corral", 43);
INSERT INTO communes VALUES(289, "Paillaco", 43);
INSERT INTO communes VALUES(290, "Los Lagos", 43);
INSERT INTO communes VALUES(291, "Panguipulli", 43);

INSERT INTO communes VALUES(292, "La Unión", 44);
INSERT INTO communes VALUES(293, "Río Bueno", 44);
INSERT INTO communes VALUES(294, "Lago Ranco", 44);
INSERT INTO communes VALUES(295, "Futrono", 44);

INSERT INTO communes VALUES(296, "Ancud", 47);
INSERT INTO communes VALUES(297, "Castro", 47);
INSERT INTO communes VALUES(298, "Chonchi", 47);
INSERT INTO communes VALUES(299, "Curaco de Velez", 47);
INSERT INTO communes VALUES(300, "Dalcahue", 47);
INSERT INTO communes VALUES(301, "Puqueldon", 47);
INSERT INTO communes VALUES(302, "Queilen", 47);
INSERT INTO communes VALUES(303, "Quemchi", 47);
INSERT INTO communes VALUES(304, "Quellon", 47);
INSERT INTO communes VALUES(305, "Quinchao", 47);

INSERT INTO communes VALUES(306, "Calbuco", 46);
INSERT INTO communes VALUES(307, "Cochamo", 46);
INSERT INTO communes VALUES(308, "Fresia", 46);
INSERT INTO communes VALUES(309, "Frutillar", 46);
INSERT INTO communes VALUES(310, "Llanquihue", 46);
INSERT INTO communes VALUES(311, "Los Muermos", 46);
INSERT INTO communes VALUES(312, "Maullin", 46);
INSERT INTO communes VALUES(313, "Puerto Montt", 46);
INSERT INTO communes VALUES(314, "Puerto Varas", 46);

INSERT INTO communes VALUES(315, "Osorno", 45);
INSERT INTO communes VALUES(316, "Puerto Octay", 45);
INSERT INTO communes VALUES(317, "Purranque", 45);
INSERT INTO communes VALUES(318, "Puyehue", 45);
INSERT INTO communes VALUES(319, "Rio Negro", 45);
INSERT INTO communes VALUES(320, "San Juan de la Costa", 45);
INSERT INTO communes VALUES(321, "San Pablo", 45);

INSERT INTO communes VALUES(322, "Chaiten", 48);
INSERT INTO communes VALUES(323, "Futaleufu", 48);
INSERT INTO communes VALUES(324, "Hualaihue", 48);
INSERT INTO communes VALUES(325, "Palena", 48);

INSERT INTO communes VALUES(326, "Cisnes", 50);
INSERT INTO communes VALUES(327, "Guaitecas", 50);
INSERT INTO communes VALUES(328, "Aysen", 50);

INSERT INTO communes VALUES(329, "Cochrane", 52);
INSERT INTO communes VALUES(330, "O'Higgins", 52);
INSERT INTO communes VALUES(331, "Tortel", 52);

INSERT INTO communes VALUES(332, "Coyhaique", 49);
INSERT INTO communes VALUES(333, "Lago Verde", 49);

INSERT INTO communes VALUES(334, "Chile Chico", 51);
INSERT INTO communes VALUES(335, "Rio Ibañez", 51);

INSERT INTO communes VALUES(336, "Antartica", 56);
INSERT INTO communes VALUES(337, "Cabo de Hornos", 56);

INSERT INTO communes VALUES(338, "Laguna Blanca", 54);
INSERT INTO communes VALUES(339, "Punta Arenas", 54);
INSERT INTO communes VALUES(340, "Rio Verde", 54);
INSERT INTO communes VALUES(341, "San Gregorio", 54);

INSERT INTO communes VALUES(342, "Porvenir", 55);
INSERT INTO communes VALUES(343, "Primavera", 55);
INSERT INTO communes VALUES(344, "Timaukel", 55);

INSERT INTO communes VALUES(345, "Natales", 53);
INSERT INTO communes VALUES(346, "Torres del Paine", 53);

-- Categorias

INSERT INTO categories VALUES(1, "Flores", "plantas de pequeño tamaño con una gran variedad de colores");
INSERT INTO categories VALUES(2, "Arboles", "plantas de gran tamaño y altura con una gra copa en su parte superior");
INSERT INTO categories VALUES(3, "Arbustos", "plantas de mediano tamaño con una gran variedad de formas");
INSERT INTO categories VALUES(4, "Herramientas", "utencilios para la jardineria");

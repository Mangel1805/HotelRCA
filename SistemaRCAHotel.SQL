/*
Created: 24/07/2015
Modified: 24/07/2015
Model: SistemaRCAHotel
Database: PostgreSQL 9.3
*/


-- Create tables section -------------------------------------------------

-- Table persona

CREATE TABLE "persona"(
 "id_persona" Serial NOT NULL,
 "perNombre" Character varying(40) NOT NULL,
 "perApellido" Character varying(40) NOT NULL,
 "perFechaNacimiento" Date NOT NULL,
 "perEmail" Character varying(60) NOT NULL,
 "perDireccion" Character varying(70) NOT NULL,
 "perCiudad" Character varying(30) NOT NULL,
 "perTelefono" Character varying(10),
 "perEstado" Boolean NOT NULL,
 "perTipo" Character varying(20) NOT NULL,
 "id_identidad" Integer
)
;

-- Create indexes for table persona

CREATE INDEX "IX_Relationship1" ON "persona" ("id_identidad")
;

-- Add keys for table persona

ALTER TABLE "persona" ADD CONSTRAINT "Key1" PRIMARY KEY ("id_persona")
;

-- Table tipo_Identidad

CREATE TABLE "tipo_Identidad"(
 "id_identidad" Serial NOT NULL,
 "nom_identidad" Character varying(15) NOT NULL
)
;

-- Add keys for table tipo_Identidad

ALTER TABLE "tipo_Identidad" ADD CONSTRAINT "Key2" PRIMARY KEY ("id_identidad")
;

-- Table cliente

CREATE TABLE "cliente"(
 "id_cliente" Integer NOT NULL,
 "cli_ocupacion" Character varying(20) NOT NULL,
 "cli_estado" Boolean NOT NULL
)
;

-- Add keys for table cliente

ALTER TABLE "cliente" ADD CONSTRAINT "Key3" PRIMARY KEY ("id_cliente")
;

-- Table servicio_cliente

CREATE TABLE "servicio_cliente"(
 "id_servicio" Serial NOT NULL,
 "id_cliente" Integer NOT NULL,
 "id_productos" Integer,
 "ser_total" Double precision NOT NULL
)
;

-- Create indexes for table servicio_cliente

CREATE INDEX "IX_Relationship4" ON "servicio_cliente" ("id_cliente")
;

CREATE INDEX "IX_Relationship20" ON "servicio_cliente" ("id_productos")
;

-- Add keys for table servicio_cliente

ALTER TABLE "servicio_cliente" ADD CONSTRAINT "Key4" PRIMARY KEY ("id_servicio")
;

-- Table factura

CREATE TABLE "factura"(
 "id_factura" Serial NOT NULL,
 "fac_subtotal" Double precision NOT NULL,
 "fac_iva" Double precision NOT NULL,
 "fac_total" Double precision NOT NULL,
 "fac_estado" Boolean NOT NULL,
 "id_recervacion" Integer NOT NULL,
 "id_servicio" Integer
)
;

-- Create indexes for table factura

CREATE INDEX "IX_Relationship5" ON "factura" ("id_servicio")
;

-- Add keys for table factura

ALTER TABLE "factura" ADD CONSTRAINT "Key5" PRIMARY KEY ("id_factura","id_recervacion")
;

-- Table empleado

CREATE TABLE "empleado"(
 "id_persona" Integer NOT NULL,
 "id_rol" Integer
)
;

-- Create indexes for table empleado

CREATE INDEX "IX_Relationship7" ON "empleado" ("id_rol")
;

-- Add keys for table empleado

ALTER TABLE "empleado" ADD CONSTRAINT "Key6" PRIMARY KEY ("id_persona")
;

-- Table rol

CREATE TABLE "rol"(
 "id_rol" Serial NOT NULL,
 "rol_nombre" Character varying(30) NOT NULL,
 "rol_descripcion" Character varying(60) NOT NULL
)
;

-- Add keys for table rol

ALTER TABLE "rol" ADD CONSTRAINT "Key7" PRIMARY KEY ("id_rol")
;

-- Table menu_opciones

CREATE TABLE "menu_opciones"(
 "id_menu_options" Serial NOT NULL,
 "men_descripcion" Character varying(50) NOT NULL,
 "id_parent_menu_options" Bigint,
 "men_url" Character varying(80) NOT NULL,
 "id_rol" Integer NOT NULL
)
;

-- Add keys for table menu_opciones

ALTER TABLE "menu_opciones" ADD CONSTRAINT "Key8" PRIMARY KEY ("id_menu_options","id_rol")
;

-- Table usuario

CREATE TABLE "usuario"(
 "usu_nick_name" Character varying(16) NOT NULL,
 "usu_clave" Character varying(60) NOT NULL,
 "usu_tipo" Character varying(20) NOT NULL,
 "id_persona" Integer NOT NULL
)
;

-- Add keys for table usuario

ALTER TABLE "usuario" ADD CONSTRAINT "Key9" PRIMARY KEY ("id_persona")
;

-- Table ingresos

CREATE TABLE "ingresos"(
 "id_ingreso" Serial NOT NULL,
 "ing_fecha" Date NOT NULL,
 "ing_detalle" Character varying(70) NOT NULL,
 "ing_tipo" Character varying(40) NOT NULL,
 "ing_valor" Double precision NOT NULL,
 "ing_status" Boolean NOT NULL,
 "id_persona" Integer
)
;

-- Create indexes for table ingresos

CREATE INDEX "IX_Relationship10" ON "ingresos" ("id_persona")
;

-- Add keys for table ingresos

ALTER TABLE "ingresos" ADD CONSTRAINT "Key10" PRIMARY KEY ("id_ingreso")
;

-- Table egresos

CREATE TABLE "egresos"(
 "id_egreso" Serial NOT NULL,
 "egr_fecha" Date NOT NULL,
 "egr_articulo" Character varying(50) NOT NULL,
 "egr_tipo" Character varying(30) NOT NULL,
 "egr_detalle" Character varying(80) NOT NULL,
 "egr_cantidad" Integer NOT NULL,
 "egr_precio_unitario" Double precision NOT NULL,
 "egr_precio_total" Double precision NOT NULL,
 "egr_status" Boolean NOT NULL,
 "id_persona" Integer
)
;

-- Create indexes for table egresos

CREATE INDEX "IX_Relationship11" ON "egresos" ("id_persona")
;

-- Add keys for table egresos

ALTER TABLE "egresos" ADD CONSTRAINT "Key11" PRIMARY KEY ("id_egreso")
;

-- Table datos_hotel

CREATE TABLE "datos_hotel"(
 "dat_ruc" Character varying(13) NOT NULL,
 "dat_direccion" Character varying(70) NOT NULL,
 "dat_telefono" Character varying(10) NOT NULL,
 "dat_organigrama" Character varying(60) NOT NULL,
 "id_persona" Integer NOT NULL
)
;

-- Add keys for table datos_hotel

ALTER TABLE "datos_hotel" ADD CONSTRAINT "Key12" PRIMARY KEY ("id_persona")
;

-- Table recervacion

CREATE TABLE "recervacion"(
 "id_recervacion" Serial NOT NULL,
 "id_cliente" Integer NOT NULL,
 "id_hab_numero" Integer NOT NULL,
 "rec_fecha_inicio" Date NOT NULL,
 "rec_fecha_fin" Date NOT NULL,
 "rec_estado" Boolean,
 "id_persona" Integer
)
;

-- Create indexes for table recervacion

CREATE INDEX "IX_Relationship13" ON "recervacion" ("id_cliente")
;

CREATE INDEX "IX_Relationship14" ON "recervacion" ("id_persona")
;

CREATE INDEX "IX_Relationship18" ON "recervacion" ("id_hab_numero")
;

-- Add keys for table recervacion

ALTER TABLE "recervacion" ADD CONSTRAINT "Key13" PRIMARY KEY ("id_recervacion")
;

-- Table habitacion

CREATE TABLE "habitacion"(
 "id_hab_numero" Serial NOT NULL,
 "id_categoria" Integer,
 "id_tip_hab" Integer,
 "hab_precio" Double precision NOT NULL,
 "hab_estado" Boolean NOT NULL
)
;

-- Create indexes for table habitacion

CREATE INDEX "IX_Relationship15" ON "habitacion" ("id_categoria")
;

CREATE INDEX "IX_Relationship17" ON "habitacion" ("id_tip_hab")
;

-- Add keys for table habitacion

ALTER TABLE "habitacion" ADD CONSTRAINT "Key14" PRIMARY KEY ("id_hab_numero")
;

-- Table categoria

CREATE TABLE "categoria"(
 "id_categoria" Serial NOT NULL,
 "cat_nombre" Character varying(40) NOT NULL,
 "cat_descripcion" Character varying(70) NOT NULL
)
;

-- Add keys for table categoria

ALTER TABLE "categoria" ADD CONSTRAINT "Key15" PRIMARY KEY ("id_categoria")
;

-- Table tipo_habitacion

CREATE TABLE "tipo_habitacion"(
 "id_tip_hab" Serial NOT NULL,
 "tip_hab_nombre" Character varying(50) NOT NULL,
 "tip_hab_descripcion" Character varying(70) NOT NULL
)
;

-- Add keys for table tipo_habitacion

ALTER TABLE "tipo_habitacion" ADD CONSTRAINT "Key16" PRIMARY KEY ("id_tip_hab")
;

-- Table pruductos

CREATE TABLE "pruductos"(
 "id_productos" Serial NOT NULL,
 "pro_nombre" Character varying(30) NOT NULL,
 "pro_descripcion" Character varying(60) NOT NULL,
 "pro_costo" Double precision NOT NULL,
 "pro_estado" Boolean NOT NULL
)
;

-- Add keys for table pruductos

ALTER TABLE "pruductos" ADD CONSTRAINT "Key17" PRIMARY KEY ("id_productos")
;

-- Create relationships section ------------------------------------------------- 

ALTER TABLE "persona" ADD CONSTRAINT "Relationship1" FOREIGN KEY ("id_identidad") REFERENCES "tipo_Identidad" ("id_identidad") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "cliente" ADD CONSTRAINT "Relationship2" FOREIGN KEY ("id_cliente") REFERENCES "persona" ("id_persona") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "servicio_cliente" ADD CONSTRAINT "Relationship4" FOREIGN KEY ("id_cliente") REFERENCES "cliente" ("id_cliente") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "factura" ADD CONSTRAINT "Relationship5" FOREIGN KEY ("id_servicio") REFERENCES "servicio_cliente" ("id_servicio") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "empleado" ADD CONSTRAINT "Relationship6" FOREIGN KEY ("id_persona") REFERENCES "persona" ("id_persona") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "empleado" ADD CONSTRAINT "Relationship7" FOREIGN KEY ("id_rol") REFERENCES "rol" ("id_rol") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "menu_opciones" ADD CONSTRAINT "se_abre" FOREIGN KEY ("id_rol") REFERENCES "rol" ("id_rol") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "usuario" ADD CONSTRAINT "Relationship9" FOREIGN KEY ("id_persona") REFERENCES "empleado" ("id_persona") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "ingresos" ADD CONSTRAINT "Relationship10" FOREIGN KEY ("id_persona") REFERENCES "usuario" ("id_persona") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "egresos" ADD CONSTRAINT "Relationship11" FOREIGN KEY ("id_persona") REFERENCES "usuario" ("id_persona") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "datos_hotel" ADD CONSTRAINT "Relationship12" FOREIGN KEY ("id_persona") REFERENCES "usuario" ("id_persona") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "recervacion" ADD CONSTRAINT "Relationship13" FOREIGN KEY ("id_cliente") REFERENCES "cliente" ("id_cliente") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "recervacion" ADD CONSTRAINT "Relationship14" FOREIGN KEY ("id_persona") REFERENCES "usuario" ("id_persona") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "habitacion" ADD CONSTRAINT "Relationship15" FOREIGN KEY ("id_categoria") REFERENCES "categoria" ("id_categoria") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "habitacion" ADD CONSTRAINT "Relationship17" FOREIGN KEY ("id_tip_hab") REFERENCES "tipo_habitacion" ("id_tip_hab") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "recervacion" ADD CONSTRAINT "Relationship18" FOREIGN KEY ("id_hab_numero") REFERENCES "habitacion" ("id_hab_numero") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "factura" ADD CONSTRAINT "Relationship19" FOREIGN KEY ("id_recervacion") REFERENCES "recervacion" ("id_recervacion") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "servicio_cliente" ADD CONSTRAINT "Relationship20" FOREIGN KEY ("id_productos") REFERENCES "pruductos" ("id_productos") ON DELETE NO ACTION ON UPDATE NO ACTION
;






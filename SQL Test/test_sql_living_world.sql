-- Create Database
create database	sql_test

-- Connect Database 
-- \c sql_test

-- Create Type for enum
create type agama as enum ('Islam', 'Kristen', 'Katolik', 'Hindu', 'Buddha', 'Konghucu');

-- Create table mahasiswa
create table mahasiswa (
  npm varchar(10) primary key unique not null, 
  nama varchar(50) not null,
  tanggal_lahir date,
  agama agama,
  alamat text,
  kota varchar(20),
  kode_pos varchar(5),
  telepon varchar(12) unique
);

-- Create table dosen
create table dosen (
  kode_dosen varchar(10) primary key unique not null, 
  nama_dosen varchar(50) not null,
  alamat text,
  kota varchar(20),
  kode_pos varchar(5),
  telepon varchar(12) unique
);

-- Create table matakuliah
create table matakuliah (
  kode_mk varchar(10) primary key unique not null, 
  nama_mk varchar(50) not null,
  sks integer not null,
  status boolean default true
);

-- Create table prestasi
create table prestasi (
  id serial primary	key, 
  npm varchar(10) not null,
  kode_mk varchar(10) not null,
  kode_dosen varchar(10) not null,
  nil_mid integer,
  nil_fin integer,
  constraint fk_mahasiswa foreign key(npm) references mahasiswa(npm),
  constraint fk_matakuliah foreign key(kode_mk) references matakuliah(kode_mk),
  constraint fk_dosen foreign key(kode_dosen) references dosen(kode_dosen)
);

-- Create table mk_dosen (many to many between table matakuliah and table dosen)
create table mk_dosen (
	id SERIAL primary key,
	kode_mk varchar(10) not null,
	kode_dosen varchar(10) not null,
	constraint fk_matakuliah foreign key(kode_mk) references matakuliah(kode_mk),
  constraint fk_dosen foreign key(kode_dosen) references dosen(kode_dosen)
);

-- Task Nomor 1 Tambahkan atribut agama pada table dosen.
alter table dosen add column agama agama;


-- Insert Data
insert into mahasiswa (npm, nama, tanggal_lahir, agama, alamat, kota, kode_pos, telepon)
values
('1234567890', 'Budi Santoso', '2000-01-01', 'Islam', 'Jl. Merdeka No. 1', 'Jakarta', '10000', '081234567890'),
('1234567891', 'Ani Rahmawati', '2000-02-02', 'Kristen', 'Jl. Sudirman No. 2', 'Bandung', '40000', '081234567891'),
('1234567892', 'Candra Wijaya', '2000-03-03', 'Hindu', 'Jl. Thamrin No. 3', 'Surabaya', '60000', '081234567892'),
('1234567893', 'Latika Nasyidah', '2000-01-01', 'Islam', 'Jl Mangga Besar 39', 'Semarang', '50000', '081234567893'),
('1234567894', 'Gada Saragih', '2000-02-02', 'Kristen', 'Jl Pahlawan Revolusi 14', 'Semarang', NULL, '081234567894'),
('1234567895', 'Elisa Lailasari', '2000-03-03', 'Islam', 'Jl Basoka 9 Sumur Batu', 'Malang', '70000', '081234567895'),
('1234567896', 'Edward Gunawan', '2000-01-01', 'Islam', 'Jl Kom L Yos Sudarso Kav 89, Dki Jakarta', 'Jakarta', NULL, '081234567896'),
('1234567897', 'Yuliana Hasanah', '2000-02-02', 'Kristen', 'Jl Delima RT 005/08 Pd Kelapa', 'Depok', '20000', '081234567897'),
('1234567898', 'Gatot Kuswoyo', '2000-03-03', 'Hindu', 'Jl Gumuruh 185, Jawa Barat', 'Bandung', '40000', '081234567898'),
('1234567899', 'Saiful Jailani', '2000-01-01', 'Islam', 'Jl. Sudirman No. 4', 'Depok', NULL, '081234567899');

insert into dosen (kode_dosen, nama_dosen, alamat, kota, kode_pos, telepon, agama)
values
('DS001', 'Dr. Andi Wijaya', 'Jl. Mawar No. 10', 'Jakarta', '10000', '081234567890', 'Islam'),
('DS002', 'Dra. Budi Lestari', 'Jl. Melati No. 20', 'Bandung', '40000', '081234567891', 'Islam'),
('DS003', 'Prof. Candra Kirana', 'Jl. Kenanga No. 30', 'Surabaya', '60000', '081234567892', 'Kristen'),
('DS004', 'Dr. Hamima Kusmawati', 'Jl Alaydrus 70 B', 'Jakarta', '10000', '081234567893', 'Islam'),
('DS005', 'Prof. Tami Nasyiah', 'Jl Industri XXIV 607', 'Semarang', '50000', '081234567894', 'Kristen');

insert into matakuliah (kode_mk, nama_mk, sks, status)
values
('TI221', 'Pengantar Teknologi Informasi', 3, TRUE),
('TI222', 'Struktur Data', 3, TRUE),
('TI223', 'Perancangan Sistem', 3, TRUE),
('TI224', 'Basis Data', 5, TRUE),
('TI225', 'Algoritma', 5, TRUE);

insert into prestasi (npm, kode_mk, kode_dosen, nil_mid, nil_fin)
values
('1234567890', 'TI221', 'DS001', 80, 90),
('1234567890', 'TI222', 'DS002', 70, 80),
('1234567890', 'TI223', 'DS003', 80, 90),
('1234567891', 'TI221', 'DS001', 80, 90),
('1234567891', 'TI222', 'DS002', 70, 80),
('1234567891', 'TI223', 'DS003', 90, 75),
('1234567892', 'TI221', 'DS001', 80, 90),
('1234567892', 'TI222', 'DS002', 70, 80),
('1234567892', 'TI223', 'DS003', 80, 90),
('1234567893', 'TI221', 'DS001', 60, 50),
('1234567893', 'TI222', 'DS002', 90, 75),
('1234567893', 'TI223', 'DS003', 80, 90),
('1234567894', 'TI221', 'DS001', 80, 90),
('1234567894', 'TI222', 'DS002', 70, 80),
('1234567894', 'TI223', 'DS003', 90, 75),
('1234567895', 'TI224', 'DS004', 40, 40),
('1234567895', 'TI225', 'DS005', 70, 59),
('1234567896', 'TI224', 'DS004', 90, 75),
('1234567896', 'TI225', 'DS005', 50, 49),
('1234567897', 'TI224', 'DS004', 70, 80),
('1234567897', 'TI225', 'DS005', 90, 75),
('1234567898', 'TI224', 'DS004', 80, 90),
('1234567898', 'TI225', 'DS005', 70, 55),
('1234567899', 'TI224', 'DS004', 70, 80),
('1234567899', 'TI225', 'DS005', 90, 75);

insert into mk_dosen (kode_mk, kode_dosen)
values 
('TI221','DS001'),
('TI222','DS002'),
('TI223','DS003'),
('TI225','DS005'),
('TI224','DS004'),
('TI224','DS002');

-- Task Nomor 2 Tampilkan semua field pada semua table mata kuliah yang mempunyai sks sama dengan 3 dan urutkan secara menurun berdasarkan nama mata kuliah.
select * from matakuliah m where sks = 3 order by nama_mk asc;

-- Task Nomor 3 Tampilkan semua field dari table biodata yang tinggal di Jakarta dan mempunyai kode pos.
select * from mahasiswa m where kota = 'Jakarta' and kode_pos is not null;

-- Task Nomor 4 Tampilkan NPM, nama dan nama mata kuliah dari mahasiswa yang memiliki nilai final lebih kecil dari 60.
select m.npm as npm, m.nama as nama_mahasiswa, m2.nama_mk as nama_mata_kuliah, p.nil_fin as nilai_final from prestasi p 
left join mahasiswa m on p.npm = m.npm 
left join matakuliah m2 on p.kode_mk = m2.kode_mk 
where p.nil_fin < 60

-- Task Nomor 5 Tampilkan NPM, nama, nama mata kuliah dan nama dosen dari mahasiswa yang mengambil mata kuliah Perancangan Sistem.
select m.npm as npm, m.nama as nama_mahasiswa, m2.nama_mk as nama_mata_kuliah, d.nama_dosen as nama_dosen from prestasi p 
left join mahasiswa m on p.npm = m.npm 
left join matakuliah m2 on p.kode_mk = m2.kode_mk 
left join dosen d on p.kode_dosen = d.kode_dosen 
where m2.nama_mk = 'Perancangan Sistem'

-- Task Nomor 6 Tampilkan NPM, nama, nama mata kuliah dan nilai total dari mahasiswa yang memiliki nilai total lebih besar dari 100 dan urutkan data berdasarkan nama mata kuliah.
select m.npm as npm, m.nama as nama_mahasiswa, m2.nama_mk as nama_mata_kuliah, p.nil_mid + p.nil_fin as nilai_total from prestasi p 
left join mahasiswa m on p.npm = m.npm 
left join matakuliah m2 on p.kode_mk = m2.kode_mk
where p.nil_mid + p.nil_fin > 100
order by m2.nama_mk asc

-- Task Nomor 7 Tampilkan nama mahasiswa, nama mata kuliah, nilai mid test dan nilai final test yang mengambil mata kuliah dengan kode ‘TI221’
select m.nama as nama_mahasiswa, m2.nama_mk as nama_mata_kuliah, p.nil_mid as nilai_mid_test, p.nil_fin as nilai_final_test from prestasi p 
left join mahasiswa m on p.npm = m.npm 
left join matakuliah m2 on p.kode_mk = m2.kode_mk
where m2.kode_mk = 'TI221'

-- Task Nomor 8 Tampilkan jumlah dari mata kuliah yang diajarkan pada table prestasi.
select count(distinct p.kode_mk) as jumlah_mata_kuliah_unique, count(p.kode_mk) as jumlah_mata_kuliah_yang_diajarkan from prestasi p 

-- Task Nomor 9 Tampilkan kode dan nama dosen yang mengajar lebih dari 1 mata kuliah.
select d.kode_dosen as kode, d.nama_dosen as nama_dosen, count(d.kode_dosen) as jumlah_mata_kuliah from mk_dosen md 
left join dosen d on md.kode_dosen = d.kode_dosen 
group by d.kode_dosen
having count(*) > 1;

-- Task Nomor 10 Tampilkan nama dan nilai mid test lebih besar dari 75 (gunakan perintah sub select).
select subsel.nama as nama, subsel.nil_mid as nilai_mid 
from (
	select * from prestasi p 
	left join mahasiswa m on p.npm = m.npm
) as subsel
where subsel.nil_mid > 75

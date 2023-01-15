CREATE TABLE `patient` (
  `patient_id` int PRIMARY KEY,
  `names` text,
  `occupation` text,
  `age` int,
  `gender` text,
  `disease` text,
  `address_location` text
);

CREATE TABLE `doctor` (
  `doctor_id` int PRIMARY KEY,
  `docotr_names` text,
  `doctor_age` int,
  `doctor_gender` text
);

CREATE TABLE `admission_discharge` (
  `id` int PRIMARY KEY,
  `ward_no` int,
  `date_of_admission` text,
  `date_of_discharge` text,
  `bill` int,
  `amount_paid` int,
  `balance` int
);

CREATE TABLE `pharmacy` (
  `pharmacy_id` int PRIMARY KEY,
  `medicine_name` text,
  `price` int
);

CREATE TABLE `treatment` (
  `patient_id` int,
  `pharmacy_id` int,
  `doctor_id` int,
  `admission_id` int
);

ALTER TABLE `treatment` ADD FOREIGN KEY (`patient_id`) REFERENCES `patient` (`patient_id`);

ALTER TABLE `treatment` ADD FOREIGN KEY (`pharmacy_id`) REFERENCES `pharmacy` (`pharmacy_id`);

ALTER TABLE `treatment` ADD FOREIGN KEY (`doctor_id`) REFERENCES `doctor` (`doctor_id`);

ALTER TABLE `treatment` ADD FOREIGN KEY (`admission_id`) REFERENCES `admission_discharge` (`id`);

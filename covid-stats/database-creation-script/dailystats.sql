USE covidstats;
CREATE TABLE dailystats(
  id INT NOT NULL AUTO_INCREMENT,
  record_date date NOT NULL,
  confirmed INT NOT NULL,
  active INT NOT NULL,
  recovered INT NOT NULL,
  deaths INT NOT NULL,
  PRIMARY KEY (id)
);
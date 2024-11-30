SET search_path TO legos;


-- Création de la table Joueuse
CREATE TABLE Joueuse (
    id_joueuse SERIAL NOT NULL  PRIMARY KEY, 
    prenom_joueuse VARCHAR(50) NOT NULL, 
    date_inscrip_joueuse DATE NOT NULL, 
    avatar_joueuse VARCHAR(255) 
);

--Création de la table cunfiguration
CREATE TABLE Cunfiguration (
    id_configuration SERIAL NOT NULL PRIMARY KEY,  
    parametres TEXT NOT NULL                       
);

-- Création de la table Partie
CREATE TABLE Partie (
    id_partie SERIAL NOT NULL PRIMARY KEY,       
    date_debut_partie DATE NOT NULL,            
    date_fin_partie DATE NOT NULL,                       
    score_partie INTEGER,                       
    id_configuration INTEGER                    
);

-- Création de la table Jouer
CREATE TABLE Jouer (
    id_joueuse INT NOT NULL,               
    id_partie INT NOT NULL,                
    gagnante BOOLEAN NOT NULL,             
    PRIMARY KEY (id_joueuse, id_partie)
);

-- Création de la table Photos
CREATE TABLE Photos (
    id_photos SERIAL PRIMARY KEY,          
    description_photo TEXT,                
    chemin_photo VARCHAR(255) NOT NULL,    
    titre_photo VARCHAR(100)               
);

--retour ici
-- Création de la table Construction
CREATE TABLE Construction (
    id_construction SERIAL PRIMARY KEY,                 
    nom_construction VARCHAR(255) NOT NULL,            
    theme_construction VARCHAR(100),                  
    description_construction TEXT,                    
    annee_sortie_construction DATE,                  
    dimensions_construction VARCHAR(50),             
    id_photos INT                          
);

-- à ajouter pour les 2 clés étrangères dans piece
ALTER TABLE piece
ADD COLUMN id_photos INT,
ADD COLUMN id_construction INT;

ALTER TABLE piece 
ADD 
FOREIGN KEY (id_photos)
REFERENCES Photos (id_photos);



ALTER TABLE piece 
ADD 
FOREIGN KEY (id_construction)
REFERENCES Construction (id_construction)
ON DELETE CASCADE;

-- Création de la table Tour
CREATE TABLE Tour (
    numero_tour INT NOT NULL,                
    id_partie INT NOT NULL,                   
    piocher BOOLEAN NOT NULL,                    
    id_joueuse INT NOT NULL,
    id INT NOT NULL,
    PRIMARY KEY (numero_tour, id_partie)                    
);



-- Création de la table Etape
CREATE TABLE Etape (
    numero_etape INT NOT NULL,                       
    id_construction INT NOT NULL,                    
    image_etape VARCHAR(255),                        
    instruction_etape TEXT,                          
    PRIMARY KEY (numero_etape, id_construction)
                               
);

-- Création de la table Usine
CREATE TABLE Usine (
    id_Usine INT NOT NULL PRIMARY KEY,  
    ville VARCHAR(100) NOT NULL,          
    pays VARCHAR(100) NOT NULL             
);

-- Création de la table Fan
CREATE TABLE Fan (
    id_Fan INT NOT NULL PRIMARY KEY,  
    ville VARCHAR(100) NOT NULL,           
    pays VARCHAR(100) NOT NULL             
);

-- Création de la table DelivrerProfessionnelle
CREATE TABLE DelivrerProfessionnelle (
    id_construction INT NOT NULL, 
    id_Usine INT NOT NULL,       
    PRIMARY KEY (id_construction, id_Usine) 
);

-- Création de la table DelivrerAmateur
CREATE TABLE DelivrerAmateur (
    id_construction INT NOT NULL, 
    id_Fan INT NOT NULL,          
    PRIMARY KEY (id_construction, id_Fan)
);


--je suis ici


--ajout des contraintes de clés, enlèves le mot CONSTRAINT
ALTER TABLE Partie
ADD 
FOREIGN KEY (id_configuration)
REFERENCES Cunfiguration (id_configuration)
ON DELETE SET NULL
ON UPDATE CASCADE;

ALTER TABLE Jouer
ADD 
FOREIGN KEY (id_joueuse)
REFERENCES Joueuse (id_joueuse)
ON DELETE CASCADE;

ALTER TABLE Jouer
ADD 
FOREIGN KEY (id_partie)
REFERENCES Partie (id_partie)
ON DELETE CASCADE;

                          
ALTER TABLE Construction                       
ADD 
FOREIGN KEY (id_photos)
REFERENCES Photos (id_photos);


ALTER TABLE Tour
ADD 
FOREIGN KEY (id_partie)
REFERENCES Partie (id_partie)
ON DELETE CASCADE ;

ALTER TABLE Tour
ADD 
FOREIGN KEY (id_joueuse)
REFERENCES Joueuse (id_joueuse)
ON DELETE CASCADE ;

ALTER TABLE Tour
ADD 
FOREIGN KEY (id) -- peut être que c'est ici le bug
REFERENCES piece (id)
ON DELETE CASCADE ;

ALTER TABLE Etape
ADD  
FOREIGN KEY (id_construction)
REFERENCES Construction (id_construction)
ON DELETE CASCADE ;

ALTER TABLE DelivrerProfessionnelle
ADD 
FOREIGN KEY (id_construction)
REFERENCES Construction (id_construction)
ON DELETE CASCADE;

ALTER TABLE DelivrerProfessionnelle
ADD 
FOREIGN KEY (id_Usine)
REFERENCES Usine (id_Usine)
ON DELETE CASCADE;

ALTER TABLE DelivrerProfessionnelle
ADD 
FOREIGN KEY (id_construction)
REFERENCES Construction (id_construction)
ON DELETE CASCADE;


ALTER TABLE DelivrerAmateur
ADD 
FOREIGN KEY (id_construction)
REFERENCES Construction (id_construction)
ON DELETE CASCADE;

ALTER TABLE DelivrerAmateur
ADD 
FOREIGN KEY (id_Fan)
REFERENCES Fan (id_Fan)
ON DELETE CASCADE ;





/*
CONSTRAINT fk_partie_configuration
CONSTRAINT fk_jouer_joueuse
CONSTRAINT fk_jouer_partie
CONSTRAINT fk_Construction_photos 
CONSTRAINT fk_tour_partie 
CONSTRAINT fk_tour_joueuse 
CONSTRAINT fk_tour_piece
CONSTRAINT fk_etape_construction
CONSTRAINT fk_Professionnelle_construction 
CONSTRAINT fk_Professionnelle_Usine 
CONSTRAINT fk_Professionnelle_construction 
CONSTRAINT fk_Amateur_construction 
CONSTRAINT fk_Amateur_fan 
CONSTRAINT fk_piece_photos 
CONSTRAINT fk_piece_construction 
*/












--nombre d'instances pour 3 tables de votre choix
--top 5 des couleurs ayant le plus de briques
-- tableau brique
--pour chaque joueuse, son score minimal et maximal
-- table jouer
--Parties avec le plus petit et le plus grand nombre de pièces défaussées, de pièces piochées
-- Tour et briques
--nombre moyen de tours, pour chaque couple(mois,année)
--table Tour et Joueuse
--top 3 des parties dans lesquelles les plus grandes pièces (longueurxlargeur) ont été placées,avec un tri décroissant sur le nombre de pièces utilisées
--table Brique et Piece

--
--lorsque c'est 0,1-0,1 on a une clé étrangère qui
--peut être d'un des deux côtés
--Brique a été remplacée par piece
--CREATE TABLE piece(
--id serial primary key,
--longueur integer,
--largeur integer,
--hauteur float,
--couleur varchar(20)
--id_photos INT, --c'est moi qui l'ajoute
--id_construction INT,
--);


-- insertion des instances fictives


-- Insertion des instances fictives dans la table Joueuse
INSERT INTO Joueuse (prenom_joueuse, date_inscrip_joueuse, avatar_joueuse)
VALUES 
    ('Alice', '2023-01-15', 'alice_avatar.png'),
    ('Bob', '2022-07-20', 'bob_avatar.png'),
    ('Charlie', '2024-03-10', 'charlie_avatar.png');


-- Insertion des instances fictives dans la table Configuration
INSERT INTO Cunfiguration (id_configuration, parametres)
VALUES 
    (1, 'Paramètre initial de test'),
    (2, 'Configuration par défaut'),
    (3, 'Paramètre avancé pour test');

-- Insertion des instances fictives dans la table Partie
INSERT INTO Partie (date_debut_partie, date_fin_partie, score_partie, id_configuration)
VALUES 
    ('2024-11-01', '2024-11-01', 150, 1),  -- Partie avec la configuration 1
    ('2024-11-02', '2024-11-02', 200, 2),  -- Partie avec la configuration 2
    ('2024-11-03', '2024-11-03', 180, 3);  -- Partie avec la configuration 3

-- Insertion des instances fictives dans la table Jouer
INSERT INTO Jouer (id_joueuse, id_partie, gagnante)
VALUES 
    (1, 1, TRUE),   -- La joueuse 1 a participé à la partie 1 et a gagné
    (2, 1, FALSE),  -- La joueuse 2 a participé à la partie 1 et a perdu
    (3, 2, TRUE);   -- La joueuse 3 a participé à la partie 2 et a gagné


-- Insertion des instances fictives dans la table Photos
INSERT INTO Photos (description_photo, chemin_photo, titre_photo)
VALUES 
    ('Photo 1', '/images/construction1.jpg', 'Construction 1'),
    ('Photo 2', '/images/construction2.jpg', 'Construction Terminée'),
    ('Photo 3', '/images/materials.jpg', 'Matériaux');

-- Insertion des instances fictives dans la table Construction
INSERT INTO Construction (nom_construction, theme_construction, description_construction, annee_sortie_construction, dimensions_construction, id_photos)
VALUES
    ('Maison en briques', 'Habitation', 'Une petite maison en briques rouges.', '2022-05-15', '10x10x5', 1),
    ('Pont en bois', 'Infrastructure', 'Un pont robuste construit en bois de chêne.', '2023-03-10', '50x5x10', 2),
    ('Tour moderne', 'Architecture', 'Une tour futuriste avec une structure en verre.', '2021-09-01', '20x20x60', 3);


-- Insertion des instances fictives dans la table Tour
INSERT INTO Tour (numero_tour, id_partie, piocher, id_joueuse, id)
VALUES
    (1, 1, TRUE, 1, 1),  -- Premier tour de la partie 1, la joueuse 1 pioche la pièce 1
    (2, 1, FALSE, 2, 2), -- Deuxième tour de la partie 1, la joueuse 2 utilise la pièce 2 sans piocher
    (1, 2, TRUE, 3, 3);  -- Premier tour de la partie 2, la joueuse 3 pioche la pièce 3



















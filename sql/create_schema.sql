CREATE DATABASE movielens_db;
USE movielens_db;

-- Movies table
CREATE TABLE movies (
    movieId INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    genres VARCHAR(255)     
);

-- Ratings table
CREATE TABLE ratings (
    ratingId INT AUTO_INCREMENT PRIMARY KEY,
    userId INT NOT NULL,
    movieId INT NOT NULL,
    rating DECIMAL(2,1) NOT NULL,
    timestamp BIGINT NOT NULL,
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);

-- Tags table
CREATE TABLE tags (
    tagId INT AUTO_INCREMENT PRIMARY KEY,
    userId INT NOT NULL,
    movieId INT NOT NULL,
    tag VARCHAR(255),
    timestamp BIGINT NOT NULL,
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);

-- Links table
CREATE TABLE links (
    movieId INT PRIMARY KEY,
    imdbId INT,
    tmdbId INT,
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);

-- Normalized genres table
CREATE TABLE movie_genres (
    movieId INT NOT NULL,
    genre VARCHAR(100) NOT NULL,
    PRIMARY KEY (movieId, genre),
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);

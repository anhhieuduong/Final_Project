import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON, Float
from sqlalchemy.sql import func

engine = create_engine(
    "sqlite:///hhvndb.db", connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Track(Base):
    __tablename__ = "tracks"

    id = Column(String, primary_key=True)
    name = Column(String)
    artist_id = Column(String, ForeignKey('artists.id'))
    release_date = Column(String)
    added_at = Column(String)

class Artist(Base):
    __tablename__ = "artists"

    id = Column(String, primary_key=True)
    name = Column(String)
    genres = Column(JSON)
    popularity = Column(Integer)
    followers = Column(Integer)
    image_url = Column(String)
    url = Column(String)

class Feature(Base):
    __tablename__ = "features"

    id = Column(String, primary_key=True)
    acousticness = Column(Float)
    danceability = Column(Float)
    duration_ms = Column(Integer)
    energy = Column(Float)
    instrumentalness = Column(Float)
    key = Column(Integer)
    liveness = Column(Float)
    loudness = Column(Float)
    mode = Column(Integer)
    speechiness = Column(Float)
    tempo = Column(Float)
    time_signature = Column(Integer)
    valence = Column(Float)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    df_artists = 'data/hhvn/df_artists_hhvn.csv'
    df_artists = pd.read_csv(df_artists)

    for index, row in df_artists.iterrows():
        artist = Artist(
            id=row['artist_id'], 
            name=row['name'], 
            genres=row['genres'],
            popularity=row['popularity'], 
            followers=row['followers'], 
            image_url=row['image_url'], 
            url=row['url']
        )
        try:
            db.add(artist)
            db.commit()
        except Exception as e:
            db.rollback() 
            print(f"Error adding artist {row['name']}: {e}")

    db.close()

    df_audio_features = 'data/hhvn/df_audio_features_hhvn.csv'
    df_audio_features = pd.read_csv(df_audio_features)

    for index, row in df_audio_features.iterrows():
        audio_features = Feature(id = row['id'], danceability = row['danceability'], energy = row['energy'], key = row['key'],
                                 loudness = row['loudness'], mode = row['mode'], speechiness = row['speechiness'],
                                 acousticness = row['acousticness'], instrumentalness = row['instrumentalness'], liveness = row['liveness'],
                                 valence = row['valence'], tempo = row['tempo'])
        db.add(audio_features)
    db.commit()

    df_tracks = 'data/hhvn/df_tracks_hhvn.csv'
    df_tracks = pd.read_csv(df_tracks)
    
    for index, row in df_tracks.iterrows():
        tracks = Track(id = row['track_id'], name = row['track_name'], artist_id = row['artist_id'], release_date = row['release_date'], added_at = row['added_at'])
        db.add(tracks)
    db.commit()
    
    # done added
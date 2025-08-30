from dataclasses import dataclass
#acts like decorator

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str
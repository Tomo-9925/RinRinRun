from typing import List

from pydantic import BaseModel


class LandmarkVisitResponse(BaseModel):
    result: str


class LandmarkVisitRequest(BaseModel):
    landmark_id: int
    course_id: int
    img: str
    debug: str = None


class LandmarkInfo(BaseModel):
    id: int
    name: str
    pos: str
    img_path: str
    description: str

class LandmarkResponse(BaseModel):
    landmarks: List[LandmarkInfo]

class LandmarkPostResponse(BaseModel):
    result: str


class LandmarkPostRequest(BaseModel):
    name: str
    description: str
    img_path: str
    pos: str

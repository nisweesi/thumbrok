from pydantic import BaseModel, Field
from typing import List


class Segment(BaseModel):
    index: int = Field(..., description="Segment index in transcript")
    start: float = Field(..., description="Start time in seconds")
    end: float = Field(..., description="End time in seconds")
    content: str = Field(..., description="Transcribed text of the segment")


class TranscriptionFormat(BaseModel):
    """
    Payload to send to Grok: full video transcription with timestamps.
    """

    filename: str = Field(..., description="Original video filename")
    language: str = Field(..., description="Language code of the transcript")
    text: str = Field(..., description="Full concatenated transcript text")
    segments: List[Segment] = Field(
        ..., description="List of segmented transcripts with timestamps"
    )


class MomentCandidate(BaseModel):
    start: float = Field(..., description="Start time of the moment in seconds")
    end: float = Field(..., description="End time of the moment in seconds")
    reason: str = Field(
        ..., description="Brief description or rationale for the selected moment"
    )
    thumbnail_text: str = Field(
        ..., description="Short thumbnail text for the thumbnail"
    )
    visual_idea: str = Field(
        ..., description="Suggested visual direction for the thumbnail"
    )


class MomentsResponseFormat(BaseModel):
    """
    Expected response from Grok: top moments with timestamps for clipping.
    """

    video_topic: str = Field(..., description="Topic or subject of the video")
    moments: List[MomentCandidate] = Field(
        ..., description="List of selected viral moments"
    )


class MomentWithImage(BaseModel):
    start: float
    end: float
    reason: str
    image_path: str
    thumbnail_text: str = Field(
        ..., description="Short thumbnail text for the thumbnail"
    )
    visual_idea: str = Field(
        ..., description="Suggested visual direction for the thumbnail"
    )


class MomentWithPrompt(BaseModel):
    start: float
    end: float
    reason: str
    image_path: str
    image_prompt: str
    thumbnail_text: str = Field(
        ..., description="Short thumbnail text for the thumbnail"
    )
    visual_idea: str = Field(
        ..., description="Suggested visual direction for the thumbnail"
    )


class SnippetFormat(BaseModel):
    image_path: str


class SnippetResponseFormat(BaseModel):
    image_prompt: str = Field(
        ...,
        description="the prompt that will be sent to Grok Imagine with the snippet to generate the thumbnail",
    )

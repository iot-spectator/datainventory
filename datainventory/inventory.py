# Copyright © 2021, 2025 by IoT Spectator. All rights reserved.

"""The main module of Data Inventory."""

import dataclasses
import datetime
import enum
import pathlib

from typing import Optional


class MediaType(enum.Enum):
    """Supported media types."""

    Image = enum.auto()
    Video = enum.auto()


@dataclasses.dataclass
class ImageMetadata:
    """Metadata for media files."""

    name: str


@dataclasses.dataclass
class VideoMetadata:
    """Metadata for video files."""

    name: str
    duration: Optional[datetime.timedelta] = None
    resolution: Optional[str] = None


@dataclasses.dataclass
class Media:
    name: str
    path: pathlib.Path
    media_type: MediaType
    size: int
    metadata: Optional[ImageMetadata | VideoMetadata] = None
    description: Optional[str] = None
    inserted_at: Optional[datetime.datetime] = None


class Inventory:

    def __init__(self):
        pass

    def insert(self, media: Media):
        """Insert media data into the inventory."""
        # Implementation for inserting media data
        pass

    def delete(self, name: str):
        """Delete media data from the inventory by name."""
        # Implementation for deleting media data
        pass

    def search(self, name: Optional[str] = None) -> list[Media]:
        """Search media data in the inventory by name."""
        # Implementation for searching media data
        return []

    def query(self, name: Optional[str] = None) -> list[Media]:
        """Query media data from the inventory."""
        # Implementation for querying media data
        return []

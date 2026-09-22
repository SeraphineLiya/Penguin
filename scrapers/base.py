from dataclasses import dataclass
from datetime import datetime


@dataclass
class Item:
    id: str
    title: str
    url: str
    source: str
    created_at: datetime
    # TODO: placeholder fields — replace/extend once you know your real data shape
    # e.g. major: str, deadline: datetime, org_name: str
    extra_field_1: str = ""
    extra_field_2: str = ""

"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeDomainReplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_name


class DescribeDomainReplicationRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainReplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDomainReplicationRequest:
    out: DescribeDomainReplicationRequest = {}  # type: ignore[typeddict-item]
    return out

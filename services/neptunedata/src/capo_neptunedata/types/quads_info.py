"""Generated from Smithy shape ``com.amazonaws.neptunedata#QuadsInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.storage_metrics


class QuadsInfo(TypedDict, closed=True):
    spog: NotRequired["capo_neptunedata.types.storage_metrics.StorageMetrics"]
    """<p>Size and count information for the SPOG quad index.</p>"""
    pogs: NotRequired["capo_neptunedata.types.storage_metrics.StorageMetrics"]
    """<p>Size and count information for the POGS quad index.</p>"""
    gpso: NotRequired["capo_neptunedata.types.storage_metrics.StorageMetrics"]
    """<p>Size and count information for the GPSO quad index.</p>"""
    osgp: NotRequired["capo_neptunedata.types.storage_metrics.StorageMetrics"]
    """<p>Size and count information for the OSGP quad index. This index is optional. For details on how to enable it and evaluate the benefits and costs, see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-data-model.html">Neptune Data Model</a>.</p>"""
    pzsog: NotRequired["capo_neptunedata.types.storage_metrics.StorageMetrics"]
    """<p>Size and count information for the PZSOG quad index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuadsInfo) -> dict:
    out: dict = {}
    if "spog" in value:
        import capo_neptunedata.types.storage_metrics

        out["SPOG"] = capo_neptunedata.types.storage_metrics.serialize_json(
            value["spog"]
        )
    if "pogs" in value:
        import capo_neptunedata.types.storage_metrics

        out["POGS"] = capo_neptunedata.types.storage_metrics.serialize_json(
            value["pogs"]
        )
    if "gpso" in value:
        import capo_neptunedata.types.storage_metrics

        out["GPSO"] = capo_neptunedata.types.storage_metrics.serialize_json(
            value["gpso"]
        )
    if "osgp" in value:
        import capo_neptunedata.types.storage_metrics

        out["OSGP"] = capo_neptunedata.types.storage_metrics.serialize_json(
            value["osgp"]
        )
    if "pzsog" in value:
        import capo_neptunedata.types.storage_metrics

        out["PZSOG"] = capo_neptunedata.types.storage_metrics.serialize_json(
            value["pzsog"]
        )
    return out


def deserialize_json(data: dict) -> QuadsInfo:
    out: QuadsInfo = {}  # type: ignore[typeddict-item]
    if data.get("SPOG") is not None:
        import capo_neptunedata.types.storage_metrics

        out["spog"] = capo_neptunedata.types.storage_metrics.deserialize_json(
            data["SPOG"]
        )
    if data.get("POGS") is not None:
        import capo_neptunedata.types.storage_metrics

        out["pogs"] = capo_neptunedata.types.storage_metrics.deserialize_json(
            data["POGS"]
        )
    if data.get("GPSO") is not None:
        import capo_neptunedata.types.storage_metrics

        out["gpso"] = capo_neptunedata.types.storage_metrics.deserialize_json(
            data["GPSO"]
        )
    if data.get("OSGP") is not None:
        import capo_neptunedata.types.storage_metrics

        out["osgp"] = capo_neptunedata.types.storage_metrics.deserialize_json(
            data["OSGP"]
        )
    if data.get("PZSOG") is not None:
        import capo_neptunedata.types.storage_metrics

        out["pzsog"] = capo_neptunedata.types.storage_metrics.deserialize_json(
            data["PZSOG"]
        )
    return out

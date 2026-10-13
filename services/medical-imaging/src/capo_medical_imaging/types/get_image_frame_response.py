"""Generated from Smithy shape ``com.amazonaws.medicalimaging#GetImageFrameResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.payload_blob


class GetImageFrameResponse(TypedDict, closed=True):
    image_frame_blob: "capo_medical_imaging.types.payload_blob.PayloadBlob"
    """<p>The blob containing the aggregated image frame information.</p>"""
    content_type: NotRequired["str"]
    """<p>The format in which the image frame information is returned to the customer. Default is <code>application/octet-stream</code>.</p> <note> <ul> <li> <p>If the stored transfer syntax is <code>1.2.840.10008.1.2.1</code>, the returned <code>contentType</code> is <code>application/octet-stream</code>.</p> </li> </ul> <ul> <li> <p>If the stored transfer syntax is <code>1.2.840.10008.1.2.4.50</code>, the returned <code>contentType</code> is <code>image/jpeg</code>.</p> </li> </ul> <ul> <li> <p>If the stored transfer syntax is <code>1.2.840.10008.1.2.4.91</code>, the returned <code>contentType</code> is <code>image/j2c</code>.</p> </li> </ul> <ul> <li> <p>If the stored transfer syntax is MPEG2, <code>1.2.840.10008.1.2.4.100</code>, <code>1.2.840.10008.1.2.4.100.1</code>, <code>1.2.840.10008.1.2.4.101</code>, or <code>1.2.840.10008.1.2.4.101.1</code>, the returned <code>contentType</code> is <code>video/mpeg</code>.</p> </li> </ul> <ul> <li> <p>If the stored transfer syntax is MPEG-4 AVC/H.264, UID <code>1.2.840.10008.1.2.4.102</code>, <code>1.2.840.10008.1.2.4.102.1</code>, <code>1.2.840.10008.1.2.4.103</code>, <code>1.2.840.10008.1.2.4.103.1</code>, <code>1.2.840.10008.1.2.4.104</code>, <code>1.2.840.10008.1.2.4.104.1</code>, <code>1.2.840.10008.1.2.4.105</code>, <code>1.2.840.10008.1.2.4.105.1</code>, <code>1.2.840.10008.1.2.4.106</code>, or <code>1.2.840.10008.1.2.4.106.1</code>, the returned <code>contentType</code> is <code>video/mp4</code>.</p> </li> </ul> <ul> <li> <p>If the stored transfer syntax is HEVC/H.265, UID <code>1.2.840.10008.1.2.4.107</code> or <code>1.2.840.10008.1.2.4.108</code>, the returned <code>contentType</code> is <code>video/H256</code>.</p> </li> </ul> <ul> <li> <p>If the stored transfer syntax is <code>1.2.840.10008.1.2.4.202</code> or if the stored transfer syntax is <i>missing</i>, the returned <code>contentType</code> is <code>image/jph</code>.</p> </li> </ul> <ul> <li> <p>If the stored transfer syntax is <code>1.2.840.10008.1.2.4.203</code>, the returned contentType is <code>image/jphc</code>.</p> </li> <li> <p>If the stored transfer syntax is <code>1.2.840.10008.1.2.4.112</code> the returned <code>contentType</code> is <code>image/jxl</code>.</p> </li> </ul> </note>"""


def redact_sensitive(value: GetImageFrameResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "image_frame_blob" in value:
        out["image_frame_blob"] = "*** Streaming Data Redacted ***"
    return out

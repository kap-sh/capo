"""Generated from Smithy shape ``com.amazonaws.mediastoredata#GetObjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediastore_data.types.content_range_pattern
    import capo_mediastore_data.types.content_type
    import capo_mediastore_data.types.e_tag
    import capo_mediastore_data.types.non_negative_long
    import capo_mediastore_data.types.payload_blob
    import capo_mediastore_data.types.status_code
    import capo_mediastore_data.types.string_primitive
    import capo_mediastore_data.types.time_stamp


class GetObjectResponse(TypedDict, closed=True):
    body: "capo_mediastore_data.types.payload_blob.PayloadBlob"
    """<p>The bytes of the object. </p>"""
    cache_control: NotRequired[
        "capo_mediastore_data.types.string_primitive.StringPrimitive"
    ]
    """<p>An optional <code>CacheControl</code> header that allows the caller to control the object's cache behavior. Headers can be passed in as specified in the HTTP spec at <a href="https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9">https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9</a>.</p> <p>Headers with a custom user-defined value are also accepted.</p>"""
    content_range: NotRequired[
        "capo_mediastore_data.types.content_range_pattern.ContentRangePattern"
    ]
    """<p>The range of bytes to retrieve.</p>"""
    content_length: NotRequired[
        "capo_mediastore_data.types.non_negative_long.NonNegativeLong"
    ]
    """<p>The length of the object in bytes.</p>"""
    content_type: NotRequired["capo_mediastore_data.types.content_type.ContentType"]
    """<p>The content type of the object.</p>"""
    e_tag: NotRequired["capo_mediastore_data.types.e_tag.ETag"]
    """<p>The ETag that represents a unique instance of the object.</p>"""
    last_modified: NotRequired["capo_mediastore_data.types.time_stamp.TimeStamp"]
    """<p>The date and time that the object was last modified.</p>"""
    status_code: "capo_mediastore_data.types.status_code.statusCode"
    """<p>The HTML status code of the request. Status codes ranging from 200 to 299 indicate success. All other status codes indicate the type of error that occurred.</p>"""

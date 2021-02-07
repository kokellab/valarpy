Notes about tables
==================

Assay frames and features (such as MI) are stored as MySQL binary
``blob``\ s.

Each frame in ``assay_frames`` is represented as a single big-endian
unsigned byte. To convert back, use ``utils.blob_to_byte_array(blob)``,
where ``blob`` is the Python ``bytes`` object returned directly from the
database.

Each value in ``well_features`` (each value is a frame for features like
MI) is represented as 4 consecutive bytes that constitute a single
big-endian unsigned float (IEEE 754 ``binary32``). Use
``utils.blob_to_float_array(blob)`` to convert back.

There shouldn’t be a need to insert these data from Python, so there’s
no way to convert in the forwards direction.

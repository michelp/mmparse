from mmparse import mmread


def test_mm_read_pattern():
    with mmread("test_data/karate.mtx") as r:
        header, row_iter = r
        assert header == {
            "mm_format": "coordinate",
            "mm_type": "pattern",
            "mm_storage": "symmetric",
            "nrows": 34,
            "ncols": 34,
            "nvals": 78,
        }
        assert list(row_iter) == [
            (23, 1, 0, True),
            (24, 2, 0, True),
            (25, 3, 0, True),
            (26, 4, 0, True),
            (27, 5, 0, True),
            (28, 6, 0, True),
            (29, 7, 0, True),
            (30, 8, 0, True),
            (31, 10, 0, True),
            (32, 11, 0, True),
            (33, 12, 0, True),
            (34, 13, 0, True),
            (35, 17, 0, True),
            (36, 19, 0, True),
            (37, 21, 0, True),
            (38, 31, 0, True),
            (39, 2, 1, True),
            (40, 3, 1, True),
            (41, 7, 1, True),
            (42, 13, 1, True),
            (43, 17, 1, True),
            (44, 19, 1, True),
            (45, 21, 1, True),
            (46, 30, 1, True),
            (47, 3, 2, True),
            (48, 7, 2, True),
            (49, 8, 2, True),
            (50, 9, 2, True),
            (51, 13, 2, True),
            (52, 27, 2, True),
            (53, 28, 2, True),
            (54, 32, 2, True),
            (55, 7, 3, True),
            (56, 12, 3, True),
            (57, 13, 3, True),
            (58, 6, 4, True),
            (59, 10, 4, True),
            (60, 6, 5, True),
            (61, 10, 5, True),
            (62, 16, 5, True),
            (63, 16, 6, True),
            (64, 30, 8, True),
            (65, 32, 8, True),
            (66, 33, 8, True),
            (67, 33, 9, True),
            (68, 33, 13, True),
            (69, 32, 14, True),
            (70, 33, 14, True),
            (71, 32, 15, True),
            (72, 33, 15, True),
            (73, 32, 18, True),
            (74, 33, 18, True),
            (75, 33, 19, True),
            (76, 32, 20, True),
            (77, 33, 20, True),
            (78, 32, 22, True),
            (79, 33, 22, True),
            (80, 25, 23, True),
            (81, 27, 23, True),
            (82, 29, 23, True),
            (83, 32, 23, True),
            (84, 33, 23, True),
            (85, 25, 24, True),
            (86, 27, 24, True),
            (87, 31, 24, True),
            (88, 31, 25, True),
            (89, 29, 26, True),
            (90, 33, 26, True),
            (91, 33, 27, True),
            (92, 31, 28, True),
            (93, 33, 28, True),
            (94, 32, 29, True),
            (95, 33, 29, True),
            (96, 32, 30, True),
            (97, 33, 30, True),
            (98, 32, 31, True),
            (99, 33, 31, True),
            (100, 33, 32, True),
        ]


def test_mm_read_real():
    with mmread("test_data/bcsstm03.mtx") as r:
        header, row_iter = r

        assert header == {
            "mm_format": "coordinate",
            "mm_type": "real",
            "mm_storage": "symmetric",
            "nrows": 112,
            "ncols": 112,
            "nvals": 112,
        }

        assert list(row_iter) == [
            (13, 0, 0, 28.0),
            (14, 1, 1, 28.0),
            (15, 2, 2, 4763.0),
            (16, 3, 3, 4763.0),
            (17, 4, 4, 0.2154813635),
            (18, 5, 5, 0.2154813635),
            (19, 6, 6, 0.0),
            (20, 7, 7, 0.0),
            (21, 8, 8, 0.5202101735),
            (22, 9, 9, 0.5202101735),
            (23, 10, 10, 0.0),
            (24, 11, 11, 0.0),
            (25, 12, 12, 0.60945762),
            (26, 13, 13, 0.60945762),
            (27, 14, 14, 0.0),
            (28, 15, 15, 0.0),
            (29, 16, 16, 0.60945762),
            (30, 17, 17, 0.60945762),
            (31, 18, 18, 0.0),
            (32, 19, 19, 0.0),
            (33, 20, 20, 0.60945762),
            (34, 21, 21, 0.60945762),
            (35, 22, 22, 0.0),
            (36, 23, 23, 0.0),
            (37, 24, 24, 0.60945762),
            (38, 25, 25, 0.60945762),
            (39, 26, 26, 0.0),
            (40, 27, 27, 0.0),
            (41, 28, 28, 1.0944223725),
            (42, 29, 29, 1.0944223725),
            (43, 30, 30, 0.0),
            (44, 31, 31, 0.0),
            (45, 32, 32, 0.9142063921),
            (46, 33, 33, 0.9142063921),
            (47, 34, 34, 0.0),
            (48, 35, 35, 0.0),
            (49, 36, 36, 2.3518140046),
            (50, 37, 37, 2.3518140046),
            (51, 38, 38, 0.0),
            (52, 39, 39, 0.0),
            (53, 40, 40, 2.58289689525),
            (54, 41, 41, 2.58289689525),
            (55, 42, 42, 0.0),
            (56, 43, 43, 0.0),
            (57, 44, 44, 4.0640961375),
            (58, 45, 45, 4.0640961375),
            (59, 46, 46, 27.42),
            (60, 47, 47, 27.42),
            (61, 48, 48, 6.84907905475),
            (62, 49, 49, 6.84907905475),
            (63, 50, 50, 0.0),
            (64, 51, 51, 0.0),
            (65, 52, 52, 5.1715672875),
            (66, 53, 53, 5.1715672875),
            (67, 54, 54, 0.0),
            (68, 55, 55, 0.0),
            (69, 56, 56, 3.5458184375),
            (70, 57, 57, 3.5458184375),
            (71, 58, 58, 24.78),
            (72, 59, 59, 24.78),
            (73, 60, 60, 2.7621511875),
            (74, 61, 61, 2.7621511875),
            (75, 62, 62, 0.0),
            (76, 63, 63, 0.0),
            (77, 64, 64, 1.8956859),
            (78, 65, 65, 1.8956859),
            (79, 66, 66, 0.0),
            (80, 67, 67, 0.0),
            (81, 68, 68, 2.876729),
            (82, 69, 69, 2.876729),
            (83, 70, 70, 20.72),
            (84, 71, 71, 20.72),
            (85, 72, 72, 1.8224085),
            (86, 73, 73, 1.8224085),
            (87, 74, 74, 0.0),
            (88, 75, 75, 0.0),
            (89, 76, 76, 2.26357691),
            (90, 77, 77, 2.26357691),
            (91, 78, 78, 18.28),
            (92, 79, 79, 18.28),
            (93, 80, 80, 3.235700691),
            (94, 81, 81, 3.235700691),
            (95, 82, 82, 0.0),
            (96, 83, 83, 0.0),
            (97, 84, 84, 4.39567529),
            (98, 85, 85, 4.39567529),
            (99, 86, 86, 0.0),
            (100, 87, 87, 0.0),
            (101, 88, 88, 2.310394609),
            (102, 89, 89, 2.310394609),
            (103, 90, 90, 2.29),
            (104, 91, 91, 2.29),
            (105, 92, 92, 1.54279626),
            (106, 93, 93, 1.54279626),
            (107, 94, 94, 42.31),
            (108, 95, 95, 42.31),
            (109, 96, 96, 0.44042214),
            (110, 97, 97, 0.44042214),
            (111, 98, 98, 0.0),
            (112, 99, 99, 0.0),
            (113, 100, 100, 13.71235058),
            (114, 101, 101, 13.71235058),
            (115, 102, 102, 5403.5),
            (116, 103, 103, 5403.5),
            (117, 104, 104, 0.37728736),
            (118, 105, 105, 0.37728736),
            (119, 106, 106, 0.0),
            (120, 107, 107, 0.0),
            (121, 108, 108, 0.10344976),
            (122, 109, 109, 0.10344976),
            (123, 110, 110, 0.0),
            (124, 111, 111, 0.0),
        ]


def test_mm_read_array_real():
    with mmread("test_data/array.mtx") as r:
        header, row_iter = r

        assert header == {
            "mm_format": "array",
            "mm_type": "real",
            "mm_storage": "general",
            "nrows": 3,
            "ncols": 2,
            "nvals": 6,
        }

        assert list(row_iter) == [
            (4, 0, 0, 1.0),
            (5, 1, 0, 2.0),
            (6, 2, 0, 3.0),
            (7, 0, 1, 1.0),
            (8, 1, 1, 2.0),
            (9, 2, 1, 3.0),
        ]

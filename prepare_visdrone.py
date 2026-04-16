from pathlib import Path
import shutil

ROOT = Path(r"C:\Users\adrit\OneDrive\Documents\UBCO\Y4T2\CMPE 401\Instructor_Defined\YOLO Model\data\VisDrone")

TRAIN_SRC = ROOT / "train" / "VisDrone2019-DET-train"
VAL_SRC = ROOT / "val" / "VisDrone2019-DET-val"
TEST_SRC = ROOT / "test-dev"   
# TEST-CHALLENGE usually has no labels, so we won't use it for training/validation prep
# =========================================================


def make_dirs():
    for split in ["train", "val", "test"]:
        (ROOT / "images" / split).mkdir(parents=True, exist_ok=True)
        (ROOT / "labels" / split).mkdir(parents=True, exist_ok=True)


def convert_visdrone_box_to_yolo(line, img_w, img_h):
    """
    VisDrone annotation format:
    bbox_left, bbox_top, bbox_width, bbox_height, score, category, truncation, occlusion

    YOLO format:
    class x_center y_center width height
    normalized to image width/height
    """
    parts = line.strip().split(",")
    if len(parts) < 8:
        return None

    x, y, w, h, score, category, truncation, occlusion = map(int, parts[:8])

    # Ignore invalid / ignored regions
    # In VisDrone, category 0 is ignored region
    if category == 0:
        return None

    # Convert category from 1-10 to 0-9 for YOLO
    cls = category - 1

    x_center = (x + w / 2) / img_w
    y_center = (y + h / 2) / img_h
    width = w / img_w
    height = h / img_h

    # Clamp to valid range
    x_center = min(max(x_center, 0.0), 1.0)
    y_center = min(max(y_center, 0.0), 1.0)
    width = min(max(width, 0.0), 1.0)
    height = min(max(height, 0.0), 1.0)

    return f"{cls} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}"


def process_split(src_dir: Path, split_name: str):
    images_src = src_dir / "images"
    ann_src = src_dir / "annotations"

    images_dst = ROOT / "images" / split_name
    labels_dst = ROOT / "labels" / split_name

    image_files = list(images_src.glob("*.jpg"))
    print(f"\nProcessing {split_name}: found {len(image_files)} images")

    for idx, img_path in enumerate(image_files, start=1):
        # Copy image
        dst_img = images_dst / img_path.name
        if not dst_img.exists():
            shutil.copy2(img_path, dst_img)

        # Find matching annotation
        ann_path = ann_src / f"{img_path.stem}.txt"
        dst_label = labels_dst / f"{img_path.stem}.txt"

        # Read image size without cv2/PIL by parsing JPG with Pillow fallback not available:
        # safer to use cv2 if installed
        import cv2
        img = cv2.imread(str(img_path))
        if img is None:
            print(f"Warning: could not read image {img_path}")
            continue
        img_h, img_w = img.shape[:2]

        yolo_lines = []
        if ann_path.exists():
            with open(ann_path, "r") as f:
                for line in f:
                    converted = convert_visdrone_box_to_yolo(line, img_w, img_h)
                    if converted:
                        yolo_lines.append(converted)

        with open(dst_label, "w") as f:
            f.write("\n".join(yolo_lines))

        if idx % 500 == 0 or idx == len(image_files):
            print(f"  {idx}/{len(image_files)} done")


def make_yaml():
    yaml_text = """path: .
train: images/train
val: images/val
test: images/test

names:
  0: pedestrian
  1: people
  2: bicycle
  3: car
  4: van
  5: truck
  6: tricycle
  7: awning-tricycle
  8: bus
  9: motor
"""
    yaml_path = ROOT / "visdrone.yaml"
    with open(yaml_path, "w") as f:
        f.write(yaml_text)
    print(f"\nCreated: {yaml_path}")


def main():
    print("Preparing VisDrone for YOLO...")
    make_dirs()
    process_split(TRAIN_SRC, "train")
    process_split(VAL_SRC, "val")
    process_split(TEST_SRC, "test")
    make_yaml()
    print("\nDone. YOLO dataset is ready.")


if __name__ == "__main__":
    main()
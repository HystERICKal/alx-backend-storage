-- This script reduces quantity after new order

CREATE TRIGGER decrease_items_quantity AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name=NEW.item_name;
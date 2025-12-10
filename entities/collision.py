def collide(obj1, obj2):
    if obj1.rect.colliderect(obj2.rect):
        return True
    else: return False

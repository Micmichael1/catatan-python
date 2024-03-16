# Package merupakan kumpulan dari module"
# Membuat package melalui file/new/pythonpackage
# Setelah Package terbentuk kemudian isi dengan module"

# Panggil modulenya dari package
import ecommerce.shipping
ecommerce.shipping.calc_shipping()

# Panggil method tertentu dari module dalam package
from ecommerce.shipping import calc_shipping
calc_shipping()

# Untuk memanggil beberapa method dari module tersebut
from ecommerce.shipping import calc_shipping,count_shipping
count_shipping()

# Untuk memanggil semua method dalam module tersebut
from ecommerce import shipping
shipping.calc_shipping()
shipping.count_shipping()
shipping.print_shipping()
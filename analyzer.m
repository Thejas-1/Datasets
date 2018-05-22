m = dlmread('FINAL/Heat_Equation/Recherche/recherche.csv')
s = size(m)

m = sortrows(m',1)'

a = []
for i=1:s(2)
a(i)=m(1,i)
end

a

b = []

for i=1:s(2)
b(i)=m(2,i)
end

for i=2:s(2)
b(i)=b(i)+b(i-1)
end

b

[T,X] = meshgrid(a,b);
u=0;

for n=1:20
u = u+(80./pi).*exp(-(n).^2.*pi.^2.*T./2500).*sin((n).*pi.*X./50)./(n)+T;
surf(T,X,u);
end




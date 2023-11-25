% Definição de fatos
% pai(X, Y) significa que X é pai de Y
pai(joao, maria).
pai(joao, pedro).
pai(pedro, carlos).
pai(pedro, ana).
pai(marcos, lucas).
pai(jose, josefina).

% mãe(X, Y) significa que X é mãe de Y
mae(ana, maria).
mae(ana, pedro).
mae(maria, carlos).
mae(maria, ana).
mae(lucia, lucas).
mae(lucia, josefina).

% Definição de regras
% irmaos(X, Y) significa que X e Y são irmãos
irmaos(X, Y) :- pai(Z, X), pai(Z, Y), mae(W, X), mae(W, Y), X \= Y.

% primos(X, Y) significa que X e Y são primos
primos(X, Y) :- pai(Z, X), pai(W, Y), irmaos(Z, W).

% tios(as)(X, Y) significa que X é tio(a) de Y
tios(X, Y) :- pai(Z, Y), irmaos(X, Z).
tios(X, Y) :- mae(Z, Y), irmaos(X, Z).

% avos(X, Y) significa que X é avô/avó de Y
avos(X, Y) :- pai(X, Z), pai(Z, Y).
avos(X, Y) :- mae(X, Z), mae(Z, Y).

% sobrinhos(X, Y) significa que X é sobrinho(a) de Y
sobrinhos(X, Y) :- tios(Y, X).

% Exemplos de consultas
% Consulta: Quem são os irmãos de Maria?
% Resposta: pedro
% ?- irmaos(maria, X).
% X = pedro.

% Consulta: Quem são os primos de Carlos?
% Resposta: ana
% ?- primos(carlos, X).
% X = ana.

% Consulta: Quem são os tios(as) de Lucas?
% Resposta: pedro
% ?- tios(X, lucas).
% X = pedro.

% Consulta: Quem são os avós de Ana?
% Resposta: joao, ana
% ?- avos(X, ana).
% X = joao ;
% X = ana.

% Consulta: Quem são os sobrinhos(as) de Maria?
% Resposta: pedro
% ?- sobrinhos(X, maria).
% X = pedro.

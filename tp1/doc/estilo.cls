\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{estilo}
\LoadClass[10pt]{article}

\RequirePackage{hyperref}
\RequirePackage{verbatim}
\RequirePackage{attachfile2}
\RequirePackage{etoolbox}
\RequirePackage{xparse}
\RequirePackage{pgffor}
\RequirePackage{arrayjobx}
\RequirePackage{graphicx}
\RequirePackage{fancyhdr}
\RequirePackage{lastpage}
\RequirePackage[document]{ragged2e}
\RequirePackage{lipsum}
\RequirePackage{translations}
\RequirePackage{ifthen}
\RequirePackage{xstring}
\RequirePackage[a4paper, left=30mm, right=30mm, top=30mm, bottom=30mm, marginpar=25mm]{geometry}
\RequirePackage[utf8]{inputenc}
\RequirePackage{csquotes}


\RequirePackage{tikz}

\RequirePackage{xfp}

% Función para poner los asteriscos
\newcommand{\andreas}[5][1.0]{
    \begin{scope}[shift={(#2,#3)},rotate=45,scale=#4,transparency group,opacity=#1]
        \fill[fill=#5] (0,0) -- (0,1) -- (3,1) -- (3,0);
        \fill[fill=#5] (1,-1) -- (2,-1) -- (2,2) -- (1,2);
    \end{scope}
}

\newcommand{\andreasline}{
    \centering\begin{tikzpicture}
        \newcommand\numcross{29}
        \foreach \n in {1,...,\the\numexpr\numcross\relax} {
            \andreas[\fpeval{0.9*sin((\n + 1)*pi/(\numcross+2))}]{0.5*\n}{0}{0.10}{black}
        }
    \end{tikzpicture}
}

\newcommand{\andreaslineslim}{
    \centering\begin{tikzpicture}[baseline]
        \newcommand\numcross{74}
        \foreach \n in {1,...,\the\numexpr\numcross\relax} {
            \andreas[0.75]{0.2*\n}{0}{0.04}{black}
        }
    \end{tikzpicture}
}

%------------------------------------------------------------------------------
%	Función para contar palabras
%------------------------------------------------------------------------------
%\newcommand{\quickwordcount}[1]{%
%  \immediate\write18{texcount -1 -sum=1,1,1,0,0,1,1. -merge -q -nobib #1.tex > #1-words.sum }%
%  \input{#1-words.sum} {palabras}%
%}
%\newcommand{\quickwordcount}[1]{%
%  \immediate\write18{texcount -1 -sum -merge #1.tex > #1-words}%
%  \input{#1-words}words%
%}
\newcommand{\quickwordcount}[1]{%
  \immediate\write18{texcount -total -sum -1 -merge #1.tex > #1-words}%
  \input{#1-words} palabras%
}


%------------------------------------------------------------------------------
%	HEADERS, FOOTERS EN SECCIONES
%------------------------------------------------------------------------------
\pagestyle{fancy}
\setlength{\headheight}{27pt}

\renewcommand{\headrulewidth}{1pt}
\renewcommand{\footrulewidth}{1pt}
\rhead{\footnotesize \textsc {Trabajo práctico 0\\ Teoría de Algoritmos}} % Trabajo práctico
\lhead{\includegraphics[width=2.5cm]{logo}}
\cfoot{\small \textsc {Página \thepage\ de \pageref*{LastPage}}}

\fancypagestyle{firststyle}
 {
  \fancyhf{}
   \renewcommand{\headrulewidth}{0pt}
   % descomentar si les interesa poner la cantidad de palabras:
   %\lfoot{\textit {\quickwordcount{main}}} 
   %\rfoot{\small \textsc {Página \thepage\ de \pageref*{LastPage}}}
 }




%------------------------------------------------------------------------------
%	CARÁTULA
%------------------------------------------------------------------------------

\renewcommand*{\maketitle}{
\thispagestyle{firststyle}
\begin{center}
\includegraphics[width=7cm]{logo}
\\[1cm]
	\textsc{\Large Teoría de Algoritmos}\\           % Materia
	\textsc{\small (75.29) Curso Buchwald - Genender}\\[0.4cm]    % Subtítulo materia
	{ \huge \bfseries Trabajo Práctico 1 \\ Algoritmos Greedy}\\[0.3cm]      % Título
	\andreasline \\[0.2cm]
	{\large \today  \\[0.4cm]}                          % Fecha
	\begin{minipage}{0.4\textwidth}
		\begin{center}
            \large{Tomas Caporaletti \\ 108598}                   % Integrante 1
		\end{center}
	\end{minipage}
 \begin{minipage}{0.4\textwidth}
		\begin{center}
            \large{Helen Chen \\ 110195}                   % Integrante 2
		\end{center}
	\end{minipage}
	\begin{minipage}{0.4\textwidth}
		\begin{center}
            \large{Lucas Garcia Campos \\ 110099}                % Integrante 3
		\end{center}
	\end{minipage}
 \end{center}
}
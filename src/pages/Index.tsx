import { useState } from "react";
import { Globe, Loader2, Copy, Trash2, ArrowRightLeft } from "lucide-react";

const LANGUAGES = [
  "English",
  "Spanish",
  "French",
  "German",
  "Chinese",
  "Hindi",
  "Japanese",
  "Korean",
  "Portuguese",
  "Italian",
  "Russian",
  "Arabic",
];

const Translator = () => {
  const [inputText, setInputText] = useState("");
  const [sourceLanguage, setSourceLanguage] = useState("English");
  const [targetLanguage, setTargetLanguage] = useState("French");
  const [translatedText, setTranslatedText] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [copied, setCopied] = useState(false);

  const handleTranslate = async () => {
    if (!inputText.trim()) return;
    setIsLoading(true);
    setTranslatedText("");

    try {
      const response = await fetch('http://localhost:5000/api/translate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text: inputText.trim(),
          source_language: sourceLanguage,
          target_language: targetLanguage,
        }),
      });

      const data = await response.json();

      if (data.success) {
        setTranslatedText(data.translated_text);
      } else {
        setTranslatedText(`Error: ${data.error}`);
      }
    } catch (error) {
      setTranslatedText(`Error: Unable to connect to translation service. Make sure the backend is running.`);
      console.error('Translation error:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleCopy = async () => {
    await navigator.clipboard.writeText(translatedText);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleClear = () => {
    setInputText("");
    setTranslatedText("");
  };

  const handleSwapLanguages = () => {
    setSourceLanguage(targetLanguage);
    setTargetLanguage(sourceLanguage);
    setTranslatedText("");
  };

  const charCount = inputText.length;
  const maxChars = 5000;

  return (
    <div className="min-h-screen bg-background gradient-bg flex flex-col">
      {/* Header */}
      <header className="pt-12 pb-6 px-4 text-center">
        <div className="flex items-center justify-center gap-3 mb-3">
          <div className="relative">
            <Globe className="w-10 h-10 text-primary" />
            <div className="absolute inset-0 w-10 h-10 rounded-full bg-primary/20 animate-pulse-glow" />
          </div>
          <h1 className="text-4xl md:text-5xl font-bold tracking-tight text-foreground">
            Trans<span className="text-gradient">Lingua</span>
          </h1>
        </div>
        <p className="text-muted-foreground text-lg font-light">
          Translate text seamlessly using AI
        </p>
      </header>

      {/* Main Card */}
      <main className="flex-1 flex items-start justify-center px-4 pb-12">
        <div className="w-full max-w-3xl glass-surface rounded-2xl p-6 md:p-8 space-y-6">
          {/* Input Area */}
          <div className="space-y-2">
            <label className="text-sm font-medium text-muted-foreground uppercase tracking-wider">
              Enter text to translate
            </label>
            <div className="relative">
              <textarea
                value={inputText}
                onChange={(e) => setInputText(e.target.value.slice(0, maxChars))}
                placeholder="Type or paste your text here..."
                rows={5}
                className="w-full bg-input/60 inner-shadow rounded-xl px-4 py-3 text-foreground placeholder:text-muted-foreground/50 resize-none focus:outline-none focus:ring-2 focus:ring-primary/40 transition-shadow duration-300 focus:glow-border-focus border border-border/50"
              />
              <span className="absolute bottom-3 right-4 text-xs text-muted-foreground/60">
                {charCount}/{maxChars}
              </span>
            </div>
          </div>

          {/* Language Selectors */}
          <div className="flex flex-col sm:flex-row items-center gap-3">
            <LanguageSelect
              label="Source"
              value={sourceLanguage}
              onChange={setSourceLanguage}
            />
            <button
              onClick={handleSwapLanguages}
              className="p-2 rounded-full bg-secondary hover:bg-secondary/80 text-primary transition-colors shrink-0"
              aria-label="Swap languages"
            >
              <ArrowRightLeft className="w-5 h-5" />
            </button>
            <LanguageSelect
              label="Target"
              value={targetLanguage}
              onChange={setTargetLanguage}
            />
          </div>

          {/* Translate Button */}
          <button
            onClick={handleTranslate}
            disabled={isLoading || !inputText.trim()}
            className="w-full gradient-primary text-primary-foreground font-semibold py-3.5 rounded-xl transition-all duration-300 hover:opacity-90 hover:shadow-[0_0_24px_-4px_hsl(var(--glow-primary)/0.5)] active:scale-[0.98] disabled:opacity-40 disabled:cursor-not-allowed flex items-center justify-center gap-2 text-lg"
          >
            {isLoading ? (
              <>
                <Loader2 className="w-5 h-5 animate-spin-slow" />
                Translating...
              </>
            ) : (
              "Translate"
            )}
          </button>

          {/* Output Area */}
          {(translatedText || isLoading) && (
            <div className="space-y-2 animate-fade-in">
              <label className="text-sm font-medium text-muted-foreground uppercase tracking-wider">
                Translated Text
              </label>
              <div className="relative bg-input/40 inner-shadow rounded-xl px-4 py-4 min-h-[80px] border border-border/30">
                {isLoading ? (
                  <div className="flex items-center gap-2 text-muted-foreground">
                    <Loader2 className="w-4 h-4 animate-spin-slow" />
                    <span className="text-sm">Translating your text...</span>
                  </div>
                ) : (
                  <p className="text-foreground text-lg leading-relaxed whitespace-pre-wrap">
                    {translatedText}
                  </p>
                )}
              </div>

              {translatedText && !isLoading && (
                <div className="flex gap-2 justify-end">
                  <button
                    onClick={handleCopy}
                    className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-secondary text-secondary-foreground text-sm hover:bg-secondary/80 transition-colors"
                  >
                    <Copy className="w-3.5 h-3.5" />
                    {copied ? "Copied!" : "Copy"}
                  </button>
                  <button
                    onClick={handleClear}
                    className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-secondary text-secondary-foreground text-sm hover:bg-secondary/80 transition-colors"
                  >
                    <Trash2 className="w-3.5 h-3.5" />
                    Clear
                  </button>
                </div>
              )}
            </div>
          )}
        </div>
      </main>

      {/* Footer */}
      <footer className="pb-6 text-center">
        <p className="text-muted-foreground/40 text-xs">
          Powered by AI · TransLingua © 2026
        </p>
      </footer>
    </div>
  );
};

const LanguageSelect = ({
  label,
  value,
  onChange,
}: {
  label: string;
  value: string;
  onChange: (v: string) => void;
}) => (
  <div className="flex-1 w-full space-y-1">
    <span className="text-xs text-muted-foreground/70 uppercase tracking-wider">
      {label}
    </span>
    <select
      value={value}
      onChange={(e) => onChange(e.target.value)}
      className="w-full bg-input/60 border border-border/50 rounded-xl px-4 py-2.5 text-foreground focus:outline-none focus:ring-2 focus:ring-primary/40 transition-shadow appearance-none cursor-pointer"
    >
      {LANGUAGES.map((lang) => (
        <option key={lang} value={lang} className="bg-card text-foreground">
          {lang}
        </option>
      ))}
    </select>
  </div>
);

export default Translator;
